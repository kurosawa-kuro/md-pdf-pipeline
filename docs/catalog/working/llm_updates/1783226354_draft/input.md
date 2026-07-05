# LLM Context Pack

## Mandatory Rules

- Do not create, overwrite, or backfill Evidence. `evidence/` is read-only Non-LLM input.
- Create `catalog_items` by repo object, not by Evidence artifact. One item key must be a file/module/symbol/entrypoint/env/dependency/test surface in the target repo.
- Evidence artifacts are inputs only. Never make `00_scan_manifest.md`, `03_symbols.md`, `30_static_signal_hits.md`, `99_scan_limitations.md`, `grep`, `change_signal`, `/`, or `src/` into a catalog item.
- Cover every relevant Evidence Index row by attaching evidence_ids to repo-object items, `scan_summary`, or `evidence_appendix`; do not silently drop evidence.
- Facts must describe the target object, not the existence of Evidence Pack files.
- Put count-only grep totals, no-hit notes, parser limitations, scan manifest/metrics/file tree, generic public API listings, and generic change signals in `scan_summary` or `evidence_appendix`, not in `catalog_items`.
- Dependency inventory and test evidence are not mere appendix when present. Create repo-object catalog items for dependency surface (`Cargo.toml` or package manifest) and test surface (`test_count`, test modules, or test files) when the evidence exists.
- A catalog item must be self-contained: an upper model must not need to open `evidence/` or `src/` to understand the object state. Do not write `refer to the evidence file`, `当該ファイルを参照`, or equivalent.
- `scan_summary` and `evidence_appendix` must also be self-contained summaries. Do not write `詳細は証拠`, `証拠を参照`, `文脈確認が必要`, or other next-action wording anywhere in the output.
- Meaning must pass the repo-specific test: could this role/implication have been written without seeing this repo? If yes, move it to appendix or rewrite it around concrete target paths/symbols.
- Add `flow_items` as first-class observed flow candidates when command/entrypoint/symbol evidence exposes connected movement. Use the name `Observed Primary Flow Candidate` conceptually, but the machine label should be descriptive such as `primary_task_lifecycle_candidate`, `destructive_management_candidate`, or `clear_all_surface_candidate`.
- Flow items are descriptive mirror material, not recommendations. Do not call a flow Golden Path or Critical User Journey as fact.
- Keep primary lifecycle and destructive management flows separate. The primary candidate must not include remove/delete/clear steps or basis entries. Clear-all is distinct from remove and must not be merged into the remove flow. If clear evidence exists, create a separate `clear_all_surface_candidate` with `flow_type: destructive_surface_candidate`; when CLI exposure is uncertain, use `surface: candidate clear operation` and put the exposure gap in `cannot_conclude`.
- Do not write real subcommand names such as `task add` unless Command variants or CLI parse evidence confirms that exact surface. If not confirmed, use candidate language such as `candidate add operation` / `candidate list operation` / `candidate status update operation`.
- Each flow must include `basis` and each step must include `user_intent`, `surface`, `components`, `data_effect`, `confidence`, and `evidence_ids` in JSON. Markdown body will render semantic fields only; evidence_ids remain machine-only. If call graph evidence is not available, set `grounding_level: weak` and put the limitation in `cannot_conclude`.
- A grep no-hit is not proof that something does not exist.
- Do not infer, reconstruct, or preserve secret values.
- Keep fact fields Non-LLM and observational; put role and current implications in meaning.
- Do not include advice, recommendations, next actions, validation plans, rollback plans, or change boundaries.

## Domain Selection Rules

- `domain` は scan profile ではなく、target の実コード・entrypoint・domain evidence から見える主対象を書く。
- `profiles_run` / `detected_profiles` に `infra` が含まれていても、それだけで `domain: infra` にしない。YAML/JSON/config は補助 evidence として扱う。
- `domain: infra` は `domain/00_infra_resources.md` に具体的な Terraform / GitHub Actions / Dockerfile resource, job, image, or secret/env reference が観測される場合だけ使う。
- `domain/00_infra_resources.md` が `status: no infra domain evidence detected` の場合、小さな CLI / library / web app の domain を infra にしない。

## Machine Provenance Boundary（重要）

JSON では、下の Evidence IDs 表にある `evidence_id` を `evidence_ids` に入れて接地を示す。存在しない id は禁止。
ただし `evidence_ids` は machine join key であり、最上位モデルの新しいアイディア・設計判断には寄与しない。
最終 Markdown 本体には program が `evidence_ids` / file / line / scan_id / sha256 を一切出さない。完全な machine provenance は `evidence_index.jsonl` sidecar に隔離する。

## Evidence IDs（catalog_items で使える evidence_id）

| evidence_id | file | lines |
|---|---|---|
| ev.00_scan_manifest_md | evidence/00_scan_manifest.md | 1-46 |
| ev.00_evidence_freshness_md | evidence/00_evidence_freshness.md | 1-12 |
| ev.01_file_tree_md | evidence/01_file_tree.md | 1-22 |
| ev.02_files_json | evidence/02_files.json | 1-22 |
| ev.03_symbols_md | evidence/03_symbols.md | 1-3 |
| ev.04_symbols_json | evidence/04_symbols.json | 1-2 |
| ev.05_tests_md | evidence/05_tests.md | 1-3 |
| ev.07_entrypoints_md | evidence/07_entrypoints.md | 1-3 |
| ev.08_config_env_md | evidence/08_config_env.md | 1-9 |
| ev.08_config_env_md.scan_limitations | evidence/08_config_env.md | 5-9 |
| ev.09_diff_evidence_md | evidence/09_diff_evidence.md | 1-56 |
| ev.09_diff_evidence_md.working_tree | evidence/09_diff_evidence.md | 5-10 |
| ev.09_diff_evidence_md.staged_files | evidence/09_diff_evidence.md | 11-16 |
| ev.09_diff_evidence_md.unstaged_files | evidence/09_diff_evidence.md | 17-22 |
| ev.09_diff_evidence_md.last_commit_files | evidence/09_diff_evidence.md | 23-42 |
| ev.09_diff_evidence_md.since_scope | evidence/09_diff_evidence.md | 43-56 |
| ev.10_observed_change_signals_md | evidence/10_observed_change_signals.md | 1-33 |
| ev.10_observed_change_signals_md.notes | evidence/10_observed_change_signals.md | 30-33 |
| ev.10_observed_change_signals_json | evidence/10_observed_change_signals.json | 1-22 |
| ev.11_dependency_inventory_md | evidence/11_dependency_inventory.md | 1-9 |
| ev.11_dependency_inventory_json | evidence/11_dependency_inventory.json | 1-2 |
| ev.12_code_metrics_md | evidence/12_code_metrics.md | 1-9 |
| ev.12_code_metrics_json | evidence/12_code_metrics.json | 1-2 |
| ev.13_public_api_surface_md | evidence/13_public_api_surface.md | 1-9 |
| ev.13_public_api_surface_json | evidence/13_public_api_surface.json | 1-2 |
| ev.14_code_excerpts_md | evidence/14_code_excerpts.md | 1-7 |
| ev.14_code_excerpts_json | evidence/14_code_excerpts.json | 1-2 |
| ev.15_decision_memory_md | evidence/15_decision_memory.md | 1-5 |
| ev.15_decision_memory_json | evidence/15_decision_memory.json | 1-3 |
| ev.domain_00_infra_resources_md | evidence/domain/00_infra_resources.md | 1-11 |
| ev.30_static_signal_hits_md | evidence/30_static_signal_hits.md | 1-22 |
| ev.30_static_signal_hits_md.guardrail | evidence/30_static_signal_hits.md | 20-22 |
| ev.98_redaction_report_md | evidence/98_redaction_report.md | 1-20 |
| ev.99_scan_limitations_md | evidence/99_scan_limitations.md | 1-18 |
| ev.99_scan_limitations_md.parser_limitations__rust | evidence/99_scan_limitations.md | 3-9 |
| ev.99_scan_limitations_md.search_limitations | evidence/99_scan_limitations.md | 10-14 |
| ev.99_scan_limitations_md.current_limits | evidence/99_scan_limitations.md | 15-18 |
| ev.grep_01_todos_md | evidence/grep/01_todos.md | 1-8 |
| ev.grep_02_job_lifecycle_md | evidence/grep/02_job_lifecycle.md | 1-6 |
| ev.grep_03_env_secret_md | evidence/grep/03_env_secret.md | 1-11 |
| ev.grep_04_high_risk_ops_md | evidence/grep/04_high_risk_ops.md | 1-8 |
| ev.grep_05_auth_permission_md | evidence/grep/05_auth_permission.md | 1-7 |
| ev.grep_06_infra_surface_md | evidence/grep/06_infra_surface.md | 1-8 |
| ev.grep_99_no_hits_md | evidence/grep/99_no_hits.md | 1-26 |
| ev.grep_99_no_hits_md.todos | evidence/grep/99_no_hits.md | 3-10 |
| ev.grep_99_no_hits_md.high_risk_ops | evidence/grep/99_no_hits.md | 11-18 |
| ev.grep_99_no_hits_md.infra_surface | evidence/grep/99_no_hits.md | 19-26 |
| ev.grep_00_queries_json | evidence/grep/00_queries.json | 1-8 |

## Evidence Inputs

### evidence/00_scan_manifest.md

```markdown
# Scan Manifest

schema_version: 1
tool_version: 0.1.0
scan_id: 20260705T043242Z_f0826d1bdc31
generated_at: 2026-07-05T04:32:42Z
tool: decision-catalog (dcm)
language: rust
root: /home/ubuntu/repos/md-pdf-pipeline
git_commit: 607993cd62b1964043debea2b1bb447148a12c45
git_branch: main
git_dirty: false
freshness_status: fresh

query_config_hash: e9dac3c3870d09c48c44a7f09c409e5a055fb41f762463fbe198c0ee6c5769aa
ignore_rules_hash: e8f0b03b63182f211b568f1e240f120892ed77d888a5fbac0075c20478e975a4
source_tree_hash: bb33f70eec2dd75209be6de288b0bcd73db94c75baf863dcef4d3af7d34d04d3
output_schema_version: 1

profile_resolution:
mode: explicit
resolver: explicit
llm_router_used: false
llm_router_is_evidence: false
candidates: rust
profiles_run: rust

requested_profiles: rust
detected_profiles: css,html,infra,python
coverage_warnings: detected `css` files outside requested profiles; detected `html` files outside requested profiles; detected `infra` files outside requested profiles; detected `python` files outside requested profiles; unsupported extensions detected: css,html,py,yaml

included_file_count: 20
symbol_count: 0
test_count: 0
entrypoint_count: 0

extractor:
  rust: syn AST exact v1 (line fallback only on parse failure)
  python: indent-heuristic v2 (public-by-convention/import/dependency inventory)
  typescript: line-heuristic v2 (export/import/dependency inventory)
  metrics: deterministic loc/symbol counts v1
  grep: substring v1

notes:
  - symbol 抽出は heuristic。macro / 動的生成は取りこぼす（99_scan_limitations.md 参照）。
  - grep no-hit は不存在の証明ではない。
```

### evidence/03_symbols.md

```markdown
# Symbols

(シンボルなし)
```

### evidence/08_config_env.md

```markdown
# Config / Env Inventory

(env 参照未検出)

## Scan Limitations

- required/optional は未確認。
- default 値は解析していない。
- secret 値は含めない。
```

### evidence/30_static_signal_hits.md

```markdown
# Static Signal Hits

This is a machine-generated signal inventory, not a decision.
Every row points back to grep evidence.

| query_id | hit_state | hits | evidence_ref | follow_up |
|---|---|---:|---|---|
| `todos` | `no_hit` | 0 | `file=evidence/grep/01_todos.md query_id=todos` | treat as no-hit, not absence |
| `job_lifecycle` | `matched` | 1 | `file=evidence/grep/02_job_lifecycle.md query_id=job_lifecycle` | review matching lines before deciding |
| `env_secret` | `matched` | 6 | `file= <REDACTED>
| `high_risk_ops` | `no_hit` | 0 | `file=evidence/grep/04_high_risk_ops.md query_id=high_risk_ops` | treat as no-hit, not absence |
| `auth_permission` | `matched` | 2 | `file=evidence/grep/05_auth_permission.md query_id=auth_permission` | review matching lines before deciding |
| `infra_surface` | `no_hit` | 0 | `file=evidence/grep/06_infra_surface.md query_id=infra_surface` | treat as no-hit, not absence |
| `change_signal:README.md` | `observed` | 4 | `file=evidence/10_observed_change_signals.md path=README.md` | inspect change history before editing |
| `change_signal:CLAUDE.md` | `observed` | 4 | `file=evidence/10_observed_change_signals.md path=CLAUDE.md` | inspect change history before editing |
| `change_signal:AGENTS.md` | `observed` | 4 | `file=evidence/10_observed_change_signals.md path=AGENTS.md` | inspect change history before editing |
| `change_signal:"doc/02_\347\247\273\350\241\214\343\203\255\343\203\274\343\203\211\343\203\236\343\203\203\343\203\227.md"` | `observed` | 2 | `file=evidence/10_observed_change_signals.md path="doc/02_\347\247\273\350\241\214\343\203\255\343\203\274\343\203\211\343\203\236\343\203\203\343\203\227.md"` | inspect change history before editing |
| `change_signal:"doc/01_\344\273\225\346\247\230\343\201\250\350\250\255\350\250\210.md"` | `observed` | 2 | `file=evidence/10_observed_change_signals.md path="doc/01_\344\273\225\346\247\230\343\201\250\350\250\255\350\250\210.md"` | inspect change history before editing |

## Guardrail

- Static signal entries are observations only. Decision Catalog claims still need explicit `evidence_ref` values.
```

### evidence/99_scan_limitations.md

```markdown
# Scan Limitations

## Parser Limitations (rust)

- シンボル抽出は行ベース heuristic であり AST ではない。
- Rust: macro / proc-macro 生成、複数行シグネチャ、conditional compilation は取りこぼす。
- Python: 動的生成 class/function、デコレータ経由の登録、import hook は静的には見えない。
- impl 内メソッドと自由関数の区別（Rust）は近似。

## Search Limitations

- grep は指定 query 語彙に依存する。no-hit は不存在の証明ではない。
- 同義語・ドメイン固有命名は取りこぼす可能性がある。

## Current Limits

- 検出したシンボルの責務は未判定（investigate / Decision Catalog で扱う）。
- env の required/optional、secret の取り扱いは未確認。
```

### evidence/evidence_index.jsonl

```markdown
{"evidence_id":"ev.00_scan_manifest_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"00_scan_manifest.md","line_start":1,"line_end":46,"sha256":"a370ad5a953ba9a02a131e0d1c8940f551951b46974a928ff4bde6308b0527d6"}
{"evidence_id":"ev.00_evidence_freshness_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"00_evidence_freshness.md","line_start":1,"line_end":12,"sha256":"b3ebacda6702bb57e01683f3792e2f191742adadb9d4557977702a0a60ff536e"}
{"evidence_id":"ev.01_file_tree_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"01_file_tree.md","line_start":1,"line_end":22,"sha256":"23a2ffaeae3a252c866c582af3fec6c09da5ba68cdfd8cb89b52954c212cc6c8"}
{"evidence_id":"ev.02_files_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"02_files.json","line_start":1,"line_end":22,"sha256":"9a681a15204e871e56b27219fa507bef961432192e5f9e478cad6a3829d33f3a"}
{"evidence_id":"ev.03_symbols_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"03_symbols.md","line_start":1,"line_end":3,"sha256":"bab7847e4a8bcf2f4146b19af49c9bdb3832cf936d773d3ca0c6eecaef3f253d"}
{"evidence_id":"ev.04_symbols_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"04_symbols.json","line_start":1,"line_end":2,"sha256":"3fbbd4c6d76130399b0c79cdf41758669224a91e05b7b216953f0c9728750865"}
{"evidence_id":"ev.05_tests_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"05_tests.md","line_start":1,"line_end":3,"sha256":"a54c8189862797477cf350a471d2a5d165d6c79a56287c9ce87b09cfdbd44780"}
{"evidence_id":"ev.07_entrypoints_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"07_entrypoints.md","line_start":1,"line_end":3,"sha256":"726464837aa1dfdb5defe2b54ba09d8e9fc5d4ca4491b6bd482336e67966ad84"}
{"evidence_id":"ev.08_config_env_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"08_config_env.md","line_start":1,"line_end":9,"sha256":"5f5583118f0939acd691ca9fe66c2e682bfe62aa8f14b737d24c77d3a6a7fe8c"}
{"evidence_id":"ev.08_config_env_md.scan_limitations","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"08_config_env.md","line_start":5,"line_end":9,"sha256":"5f5583118f0939acd691ca9fe66c2e682bfe62aa8f14b737d24c77d3a6a7fe8c"}
{"evidence_id":"ev.09_diff_evidence_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"09_diff_evidence.md","line_start":1,"line_end":56,"sha256":"149091f88cebea3b7add65561d43f53d5ff57c40088d9859a14cd05232f40e65"}
{"evidence_id":"ev.09_diff_evidence_md.working_tree","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"09_diff_evidence.md","line_start":5,"line_end":10,"sha256":"149091f88cebea3b7add65561d43f53d5ff57c40088d9859a14cd05232f40e65"}
{"evidence_id":"ev.09_diff_evidence_md.staged_files","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"09_diff_evidence.md","line_start":11,"line_end":16,"sha256":"149091f88cebea3b7add65561d43f53d5ff57c40088d9859a14cd05232f40e65"}
{"evidence_id":"ev.09_diff_evidence_md.unstaged_files","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"09_diff_evidence.md","line_start":17,"line_end":22,"sha256":"149091f88cebea3b7add65561d43f53d5ff57c40088d9859a14cd05232f40e65"}
{"evidence_id":"ev.09_diff_evidence_md.last_commit_files","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"09_diff_evidence.md","line_start":23,"line_end":42,"sha256":"149091f88cebea3b7add65561d43f53d5ff57c40088d9859a14cd05232f40e65"}
{"evidence_id":"ev.09_diff_evidence_md.since_scope","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"09_diff_evidence.md","line_start":43,"line_end":56,"sha256":"149091f88cebea3b7add65561d43f53d5ff57c40088d9859a14cd05232f40e65"}
{"evidence_id":"ev.10_observed_change_signals_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"10_observed_change_signals.md","line_start":1,"line_end":33,"sha256":"c7deaa925f238e4406180b45ce9cdb97c9f0d4951185b46836a461e70174333a"}
{"evidence_id":"ev.10_observed_change_signals_md.notes","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"10_observed_change_signals.md","line_start":30,"line_end":33,"sha256":"c7deaa925f238e4406180b45ce9cdb97c9f0d4951185b46836a461e70174333a"}
{"evidence_id":"ev.10_observed_change_signals_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"10_observed_change_signals.json","line_start":1,"line_end":22,"sha256":"b04ddd2d992a804492382e8f7fed754a004b4353bf8b7c01885768b8ab495b74"}
{"evidence_id":"ev.11_dependency_inventory_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"11_dependency_inventory.md","line_start":1,"line_end":9,"sha256":"a5d3314b54560c0f0851042eef1e7a09fa049a6d6709dd9da9f9a826eaa8d71e"}
{"evidence_id":"ev.11_dependency_inventory_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"11_dependency_inventory.json","line_start":1,"line_end":2,"sha256":"2001f2ead4f6542db1aed8b89cbace3137529a4eacf54bd10618910a5862126e"}
{"evidence_id":"ev.12_code_metrics_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"12_code_metrics.md","line_start":1,"line_end":9,"sha256":"068af7b0dc3fa331570719d9b850ce3c1b98dc54f4a0ae4ff2b8839f476817ba"}
{"evidence_id":"ev.12_code_metrics_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"12_code_metrics.json","line_start":1,"line_end":2,"sha256":"597d4e3edebaba61abdd554a501fa137d32ee714a6caee04c285878d54d813dd"}
{"evidence_id":"ev.13_public_api_surface_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"13_public_api_surface.md","line_start":1,"line_end":9,"sha256":"affe175e9c0f1aff8caa8f14f4720c30ac190f880f870bb6c69bafe103d16dc8"}
{"evidence_id":"ev.13_public_api_surface_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"13_public_api_surface.json","line_start":1,"line_end":2,"sha256":"ea4b99d19c0c38539327e545d8a67c267f774b393cbe8cfa3bcb55ea057ab2fb"}
{"evidence_id":"ev.14_code_excerpts_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"14_code_excerpts.md","line_start":1,"line_end":7,"sha256":"b6d4563a3f47f8115dea187aa50bae78a62b02bb615b4f28a6aacc039bc0de38"}
{"evidence_id":"ev.14_code_excerpts_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"14_code_excerpts.json","line_start":1,"line_end":2,"sha256":"799fbe006509478ca478f2e16157cab0fbc71eb723fcb9065416c73e3319b408"}
{"evidence_id":"ev.15_decision_memory_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"15_decision_memory.md","line_start":1,"line_end":5,"sha256":"29af5e5102a32fd734c809e6a96470dc3e083ed135b337aebfeda77b2e60c82a"}
{"evidence_id":"ev.15_decision_memory_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"15_decision_memory.json","line_start":1,"line_end":3,"sha256":"f35cb05fcf7ed2c5758ac73f1a82069f3e9d70f22546f40c84f496018da1fa82"}
{"evidence_id":"ev.domain_00_infra_resources_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"domain/00_infra_resources.md","line_start":1,"line_end":11,"sha256":"c126db844bef149683003ee51e4340d3eb5a90ac0090f8a83291676b6fb7915d"}
{"evidence_id":"ev.30_static_signal_hits_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"30_static_signal_hits.md","line_start":1,"line_end":22,"sha256":"642fd2473840ce08f8c0b7442be21e077cb3c4b53819d11a44c65e019410144b"}
{"evidence_id":"ev.30_static_signal_hits_md.guardrail","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"30_static_signal_hits.md","line_start":20,"line_end":22,"sha256":"642fd2473840ce08f8c0b7442be21e077cb3c4b53819d11a44c65e019410144b"}
{"evidence_id":"ev.98_redaction_report_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"98_redaction_report.md","line_start":1,"line_end":20,"sha256":"55800e7befaadc83919444e738cd46fd3772cd30543baf1ac37a6e58dc1313d9"}
{"evidence_id":"ev.99_scan_limitations_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"99_scan_limitations.md","line_start":1,"line_end":18,"sha256":"5796e5f1cc81bdd60e31b52df7fae5ae5a41477dcf8c84baef06f32d24e3c5f4"}
{"evidence_id":"ev.99_scan_limitations_md.parser_limitations__rust","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"99_scan_limitations.md","line_start":3,"line_end":9,"sha256":"5796e5f1cc81bdd60e31b52df7fae5ae5a41477dcf8c84baef06f32d24e3c5f4"}
{"evidence_id":"ev.99_scan_limitations_md.search_limitations","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"99_scan_limitations.md","line_start":10,"line_end":14,"sha256":"5796e5f1cc81bdd60e31b52df7fae5ae5a41477dcf8c84baef06f32d24e3c5f4"}
{"evidence_id":"ev.99_scan_limitations_md.current_limits","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"99_scan_limitations.md","line_start":15,"line_end":18,"sha256":"5796e5f1cc81bdd60e31b52df7fae5ae5a41477dcf8c84baef06f32d24e3c5f4"}
{"evidence_id":"ev.grep_01_todos_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/01_todos.md","line_start":1,"line_end":8,"sha256":"eb5c8c588ea3831e4151283bc851555d2cca5842f2b83d1b1c0063f437304eb1"}
{"evidence_id":"ev.grep_02_job_lifecycle_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/02_job_lifecycle.md","line_start":1,"line_end":6,"sha256":"7ebb9aab4a2dd7ec5ba1e8b00d1a0966e1ca996a31caa051074279e3b77d861b"}
{"evidence_id":"ev.grep_03_env_secret_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/03_env_secret.md","line_start":1,"line_end":11,"sha256":"55084aecdebe40d5ca28380ab4c77c1ac62ade36e9d5ddce6114c243bdffe7a7"}
{"evidence_id":"ev.grep_04_high_risk_ops_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/04_high_risk_ops.md","line_start":1,"line_end":8,"sha256":"b94225c72b4b88a5124a75d271cf97ecf967129ea55309bcfa1d3ad3baaa0a31"}
{"evidence_id":"ev.grep_05_auth_permission_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/05_auth_permission.md","line_start":1,"line_end":7,"sha256":"6584e6a0905b9ae4c4ddcdfa0524c0b136347f2d6e425cc3c3703415efa3dfc5"}
{"evidence_id":"ev.grep_06_infra_surface_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/06_infra_surface.md","line_start":1,"line_end":8,"sha256":"94fb2ecd02c0ecd9106060c87af7d751d1ef4853f5a561b0a89b9a95b37aa5e3"}
{"evidence_id":"ev.grep_99_no_hits_md","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/99_no_hits.md","line_start":1,"line_end":26,"sha256":"d4c5ae659cb100ed45ab94fe88ae83c76142d781f2a043e4f4d330ac9a1e8e87"}
{"evidence_id":"ev.grep_99_no_hits_md.todos","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/99_no_hits.md","line_start":3,"line_end":10,"sha256":"d4c5ae659cb100ed45ab94fe88ae83c76142d781f2a043e4f4d330ac9a1e8e87"}
{"evidence_id":"ev.grep_99_no_hits_md.high_risk_ops","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/99_no_hits.md","line_start":11,"line_end":18,"sha256":"d4c5ae659cb100ed45ab94fe88ae83c76142d781f2a043e4f4d330ac9a1e8e87"}
{"evidence_id":"ev.grep_99_no_hits_md.infra_surface","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/99_no_hits.md","line_start":19,"line_end":26,"sha256":"d4c5ae659cb100ed45ab94fe88ae83c76142d781f2a043e4f4d330ac9a1e8e87"}
{"evidence_id":"ev.grep_00_queries_json","scan_id":"20260705T043242Z_f0826d1bdc31","target_git_commit":"607993cd62b1964043debea2b1bb447148a12c45","artifact":"grep/00_queries.json","line_start":1,"line_end":8,"sha256":"e9dac3c3870d09c48c44a7f09c409e5a055fb41f762463fbe198c0ee6c5769aa"}
```

### evidence/01_file_tree.md

```markdown
# File Tree

- .gitignore
- AGENTS.md
- CLAUDE.md
- Makefile
- README.md
- doc/01_仕様と設計.md
- doc/02_移行ロードマップ.md
- doc/03_実装カタログ.md
- doc/04_運用.md
- doc/README.md
- doppler.yaml
- env/config.yaml
- requirements.txt
- src/cli.py
- src/examples/sample.md
- src/html_renderer.py
- src/markdown_loader.py
- src/pdf_renderer.py
- src/styles/print.css
- src/templates/base.html
```

### evidence/98_redaction_report.md

```markdown
# Redaction Report

status: passed
redacted_count: 0

checked_keywords:
  - secret
  - token
  - password
  - api_key
  - apikey
  - key

scope:
  - env_secret grep の代入形 (`KEY = ...` / `KEY: <REDACTED>

notes:
  - name / 参照箇所は残し、value のみ `<redacted>` に置換している。
  - これは網羅的な secret スキャンではない（高エントロピー文字列検出は対象外）。
  - env 参照の呼び出し（env::var / os.environ）は value を持たないため redaction 対象外。
```

## Investigated Findings

```markdown
# Investigated Findings

generated_by: dcm investigate
source: non_llm_evidence_investigation
judgment_status: llm_enriched

## observed_signals

- Evidence Pack exists and has the required scan, symbol, config, risk, and scan-limitation files. evidence_ref: file=evidence/00_scan_manifest.md
- Symbol evidence exists for code navigation and candidate responsibility boundaries. evidence_ref: file=evidence/03_symbols.md
- Configuration and environment evidence exists for secret and runtime-risk review. evidence_ref: file=evidence/08_config_env.md
- Static signal evidence exists and must be investigated before draft. evidence_ref: file=evidence/30_static_signal_hits.md
- Scan limitation evidence exists and can inform descriptive current implications when judgment-relevant. evidence_ref: file=evidence/99_scan_limitations.md

## available_evidence_files

- `00_evidence_freshness.md`
- `00_scan_manifest.md`
- `01_file_tree.md`
- `02_files.json`
- `03_symbols.md`
- `04_symbols.json`
- `05_tests.md`
- `07_entrypoints.md`
- `08_config_env.md`
- `09_diff_evidence.md`
- `10_observed_change_signals.json`
- `10_observed_change_signals.md`
- `11_dependency_inventory.json`
- `11_dependency_inventory.md`
- `12_code_metrics.json`
- `12_code_metrics.md`
- `13_public_api_surface.json`
- `13_public_api_surface.md`
- `14_code_excerpts.json`
- `14_code_excerpts.md`
- `15_decision_memory.json`
- `15_decision_memory.md`
- `30_static_signal_hits.md`
- `98_redaction_report.md`
- `99_scan_limitations.md`

## llm_enrichment

# Investigation Findings

## item_meaning_candidates

- The repository (`md-pdf-pipeline`) is a Rust project (language: rust, tool: decision-catalog) that likely processes Markdown to PDF, based on the project name and the presence of change signals on Markdown documentation files (e.g., `README.md`, `CLAUDE.md`, `AGENTS.md`) — see `evidence/30_static_signal_hits.md` query_ids `change_signal:README.md`, `change_signal:CLAUDE.md`, `change_signal:AGENTS.md`.  
- The codebase also contains CSS, HTML, infra, and Python files (`evidence/00_scan_manifest.md` coverage_warnings). This suggests a multi-language project where the core logic is Rust but there are supporting files for web rendering, configuration, or scripting.  
- No public API surface, entrypoints, tests, or symbols were extracted (`evidence/03_symbols.md`, `evidence/05_tests.md`, `evidence/07_entrypoints.md`). This may indicate a library, an internal tool without exposed entrypoints, or a project where symbols are generated dynamically / via macros not captured by the Rust syn AST extractor (`evidence/99_scan_limitations.md`).

## role_notes

- The project has a `main` branch and a clean git state, with a single git commit (`607993cd62b1964043debea2b1bb447148a12c45`) at the time of scan (`evidence/00_scan_manifest.md`).  
- Static signal hits include `job_lifecycle` (1 hit), `auth_permission` (2 hits), and `env_secret` (6 hits, redacted) — see `evidence/30_static_signal_hits.md`. These signals suggest the presence of job lifecycle management, authorization/permission handling, and environment secret usage. The actual lines are not provided (referenced grep files are not in the pack), so role details are unresolved.  
- Change signals are observed on multiple documentation files, indicating active development or maintenance of project docs (`evidence/10_observed_change_signals.md`, referenced in `evidence/30_static_signal_hits.md`).  
- No env references were detected in code (`evidence/08_config_env.md`), despite the `env_secret` signal. This inconsistency may be due to heuristic limitations or the redaction of secret-containing evidence.

## current_implications

- The project appears to be in an early or mature stable stage with no recent test or entrypoint additions detectable by the scan. The absence of extracted symbols and tests could be a scanner limitation rather than a codebase deficiency (`evidence/99_scan_limitations.md`).  
- Static signals point to possible security-sensitive areas (auth, secrets, job lifecycle) that may require manual review or deeper investigation before any changes.  
- The presence of unsupported file types (CSS, HTML, Python) that were not scanned under requested profiles (`rust`) means those components are not covered by this evidence pack. Their roles and dependencies are unknown, potentially affecting decision-making about the overall system.  
- Change signals on documentation files suggest that documentation is part of the active change surface and should be kept consistent with code changes.

## uncertainty_notes

- Symbol extraction is heuristic; macros, conditional compilation, and dynamic generation are likely missed (`evidence/99_scan_limitations.md` Rust section). This strongly limits the completeness of the symbol inventory.  
- Grep-based static signals are dictionary-limited; no-hit does not prove absence (`evidence/30_static_signal_hits.md` guardrail comment, `evidence/99_scan_limitations.md` search limitations).  
- The `env_secret` signal is redacted in this evidence pack; we cannot assess its content or severity.  
- The `auth_permission` and `job_lifecycle` hits have no follow-up detail beyond confirming matches — the actual matching lines are not included in the pack.  
- Coverage warnings indicate that CSS, HTML, infra, and Python files exist but were not profiled. The impact of these omitted components on the overall system is unknown.  
- No information about required / optional env configuration or default values is available (`evidence/08_config_env.md` scan limitations).

## judgment_value_added

- Raw inventory has been classified into draft inputs: observed signals, roles, and current implications.
- LLM enrichment, when present, adds meaning for each evidence item without changing observed evidence.
- This file does not approve an implementation choice or prescribe future work. It prevents raw scan output from being treated as a completed Decision Catalog.

## draft_inputs

- Draft must create `catalog_items` where each item pairs fact and meaning.
- Draft must not include advice, recommendations, next actions, validation plans, rollback plans, or change boundaries.
- Draft must cite evidence_ids for fact items and must not invent facts outside the Evidence Pack.

## required_llm_enrichment

- Assign role/current implication to evidence items.
- Keep risk language descriptive and current-state only.
- Put judgment-relevant uncertainty in descriptive current implications instead of a separate field.

## next_step

- Run `dcm draft <TARGET>` or `dcm llm draft <TARGET>` only after this investigated findings file exists.
```


---

# Investigated Findings

# Investigated Findings

generated_by: dcm investigate
source: non_llm_evidence_investigation
judgment_status: llm_enriched

## observed_signals

- Evidence Pack exists and has the required scan, symbol, config, risk, and scan-limitation files. evidence_ref: file=evidence/00_scan_manifest.md
- Symbol evidence exists for code navigation and candidate responsibility boundaries. evidence_ref: file=evidence/03_symbols.md
- Configuration and environment evidence exists for secret and runtime-risk review. evidence_ref: file=evidence/08_config_env.md
- Static signal evidence exists and must be investigated before draft. evidence_ref: file=evidence/30_static_signal_hits.md
- Scan limitation evidence exists and can inform descriptive current implications when judgment-relevant. evidence_ref: file=evidence/99_scan_limitations.md

## available_evidence_files

- `00_evidence_freshness.md`
- `00_scan_manifest.md`
- `01_file_tree.md`
- `02_files.json`
- `03_symbols.md`
- `04_symbols.json`
- `05_tests.md`
- `07_entrypoints.md`
- `08_config_env.md`
- `09_diff_evidence.md`
- `10_observed_change_signals.json`
- `10_observed_change_signals.md`
- `11_dependency_inventory.json`
- `11_dependency_inventory.md`
- `12_code_metrics.json`
- `12_code_metrics.md`
- `13_public_api_surface.json`
- `13_public_api_surface.md`
- `14_code_excerpts.json`
- `14_code_excerpts.md`
- `15_decision_memory.json`
- `15_decision_memory.md`
- `30_static_signal_hits.md`
- `98_redaction_report.md`
- `99_scan_limitations.md`

## llm_enrichment

# Investigation Findings

## item_meaning_candidates

- The repository (`md-pdf-pipeline`) is a Rust project (language: rust, tool: decision-catalog) that likely processes Markdown to PDF, based on the project name and the presence of change signals on Markdown documentation files (e.g., `README.md`, `CLAUDE.md`, `AGENTS.md`) — see `evidence/30_static_signal_hits.md` query_ids `change_signal:README.md`, `change_signal:CLAUDE.md`, `change_signal:AGENTS.md`.  
- The codebase also contains CSS, HTML, infra, and Python files (`evidence/00_scan_manifest.md` coverage_warnings). This suggests a multi-language project where the core logic is Rust but there are supporting files for web rendering, configuration, or scripting.  
- No public API surface, entrypoints, tests, or symbols were extracted (`evidence/03_symbols.md`, `evidence/05_tests.md`, `evidence/07_entrypoints.md`). This may indicate a library, an internal tool without exposed entrypoints, or a project where symbols are generated dynamically / via macros not captured by the Rust syn AST extractor (`evidence/99_scan_limitations.md`).

## role_notes

- The project has a `main` branch and a clean git state, with a single git commit (`607993cd62b1964043debea2b1bb447148a12c45`) at the time of scan (`evidence/00_scan_manifest.md`).  
- Static signal hits include `job_lifecycle` (1 hit), `auth_permission` (2 hits), and `env_secret` (6 hits, redacted) — see `evidence/30_static_signal_hits.md`. These signals suggest the presence of job lifecycle management, authorization/permission handling, and environment secret usage. The actual lines are not provided (referenced grep files are not in the pack), so role details are unresolved.  
- Change signals are observed on multiple documentation files, indicating active development or maintenance of project docs (`evidence/10_observed_change_signals.md`, referenced in `evidence/30_static_signal_hits.md`).  
- No env references were detected in code (`evidence/08_config_env.md`), despite the `env_secret` signal. This inconsistency may be due to heuristic limitations or the redaction of secret-containing evidence.

## current_implications

- The project appears to be in an early or mature stable stage with no recent test or entrypoint additions detectable by the scan. The absence of extracted symbols and tests could be a scanner limitation rather than a codebase deficiency (`evidence/99_scan_limitations.md`).  
- Static signals point to possible security-sensitive areas (auth, secrets, job lifecycle) that may require manual review or deeper investigation before any changes.  
- The presence of unsupported file types (CSS, HTML, Python) that were not scanned under requested profiles (`rust`) means those components are not covered by this evidence pack. Their roles and dependencies are unknown, potentially affecting decision-making about the overall system.  
- Change signals on documentation files suggest that documentation is part of the active change surface and should be kept consistent with code changes.

## uncertainty_notes

- Symbol extraction is heuristic; macros, conditional compilation, and dynamic generation are likely missed (`evidence/99_scan_limitations.md` Rust section). This strongly limits the completeness of the symbol inventory.  
- Grep-based static signals are dictionary-limited; no-hit does not prove absence (`evidence/30_static_signal_hits.md` guardrail comment, `evidence/99_scan_limitations.md` search limitations).  
- The `env_secret` signal is redacted in this evidence pack; we cannot assess its content or severity.  
- The `auth_permission` and `job_lifecycle` hits have no follow-up detail beyond confirming matches — the actual matching lines are not included in the pack.  
- Coverage warnings indicate that CSS, HTML, infra, and Python files exist but were not profiled. The impact of these omitted components on the overall system is unknown.  
- No information about required / optional env configuration or default values is available (`evidence/08_config_env.md` scan limitations).

## judgment_value_added

- Raw inventory has been classified into draft inputs: observed signals, roles, and current implications.
- LLM enrichment, when present, adds meaning for each evidence item without changing observed evidence.
- This file does not approve an implementation choice or prescribe future work. It prevents raw scan output from being treated as a completed Decision Catalog.

## draft_inputs

- Draft must create `catalog_items` where each item pairs fact and meaning.
- Draft must not include advice, recommendations, next actions, validation plans, rollback plans, or change boundaries.
- Draft must cite evidence_ids for fact items and must not invent facts outside the Evidence Pack.

## required_llm_enrichment

- Assign role/current implication to evidence items.
- Keep risk language descriptive and current-state only.
- Put judgment-relevant uncertainty in descriptive current implications instead of a separate field.

## next_step

- Run `dcm draft <TARGET>` or `dcm llm draft <TARGET>` only after this investigated findings file exists.


---

# Create Decision Catalog Prompt

`00_llm_context_pack.md` の Evidence と Investigated Findings に基づき、Decision Catalog の判断を
**JSON schema に厳密準拠した JSON で** 返す（response_format で強制される）。markdown は書かない。

出力構造:
- `catalog_items`: 上位モデルが読む本体。repo object のみを書く。許可 subject は file / module / symbol / entrypoint / env / dependency / test_surface。
- `flow_items`: 観測される主要フロー候補を書く。product Golden Path 判定ではなく、entrypoint / command surface / touched symbols で弱接地した記述的な動線素材。`catalog_items` は部品、`flow_items` は部品間の方向・順序・候補導線、`evidence_appendix` は scan 足場。
- `scan_summary`: count-only signal、no-hit 注記、scan manifest / metrics / file tree など、意味付け対象ではないが捨ててはいけない scan 概要を書く。
- `evidence_appendix`: parser limitation、generic public API listing、generic change_signal、infra no-hit など、本体 item にしない補助 evidence を書く。

言語ルール:
- prose フィールド（fact.detail / meaning.role / meaning.current_implication）は**日本語**で書く。
- schema のキーと enum 値（confidence, fact.type, observed_by）は英語のまま。

参照ルール（最重要）:
- catalog_items の各項目は `evidence_ids` に、Evidence Index の `evidence_id` 値だけを入れる（例: `ev.03_symbols_md`）。
- `evidence_ids` は必ず `ev.` で始まる値だけ。`item.*` / `src.*` / `path.*` のような repo-object ID を入れない。
- 単数形 `evidence_id` は schema に存在しない。必ず配列 `evidence_ids` だけを使う。
- **file / line / scan_id / sha256 は書かない**。`evidence_ids` も machine join key なので Markdown 本体へ出ない。完全な machine provenance は `evidence_index.jsonl` sidecar に隔離する。
- 存在しない evidence_id を作らない。unknown id は reject される。
- catalog_items の全項目に最低 1 つの evidence_id を付ける。

- flow_items のルール:
- `subject_kind` は必ず `evidence_inferred_flow`。
- `flow_type` は `primary_candidate` / `destructive` / `destructive_surface_candidate` / `decoy_signal` / `config` / `error` / `unknown`。`grounding_level` と step `confidence` は `strong` / `medium` / `weak`。
- `label` は `primary_task_lifecycle_candidate` / `destructive_management_candidate` / `clear_all_surface_candidate` のように観測候補として書く。`Golden Path` / `Critical User Journey` を fact 化しない。
- primary と destructive を混ぜない。primary_candidate に remove/delete/clear の step や basis を入れない。clear は remove と別 flow item にし、`flow_type: destructive_surface_candidate` を使う。CLI 露出が evidence で不明なら `surface: candidate clear operation` として弱く書き、露出ギャップを `cannot_conclude` に残す。
- 各 flow は `basis` を持つ。例: `src/cli.rs::Command`, `src/store.rs::Store::{add,tasks,set_status,remove}`, `src/model.rs::{Task,Status}`。
- 各 step は `user_intent`, `surface`, `components`, `data_effect`, `confidence`, `evidence_ids` を持つ。`components` は repo object、`basis` は根拠シンボル。本文に evidence refs や evidence_ids は出ない。
- `surface` に `task add` のような実サブコマンド名を書けるのは、Command variant / CLI parse evidence で確認できた場合だけ。未確認なら `candidate add operation` / `candidate list operation` / `candidate status update operation` と書く。
- call graph が無い場合は `grounding_level: weak` とし、`cannot_conclude` に「product 上の主要行動かは断定しない」「dispatch 順序は call graph 未導入では弱接地」「CLI サブコマンド実名は未確認」のような接地ギャップを残す。
- flow は処方ではない。守るべき、改善すべき、確認ダイアログを足すべき、`next_action` などを書かない。

- fact は target の事実だけを書く。Evidence Pack や `evidence/` のファイルが存在する、というメタ事実を書かない。

内容ルール:
- catalog_items の fact.path は `/` / 空 / `src/` / evidence artifact 名にしない。`src/cli.rs`, `src/store.rs`, `src/model.rs::Task`, `src/model.rs::Status`, `src/main.rs`, `TASKCLI_DB` のように repo object をキーにする。
- Rust CLI で該当 evidence がある場合、最低限 `src/cli.rs`, `src/store.rs`, `src/model.rs::Task`, `src/model.rs::Status`, `src/main.rs`, `TASKCLI_DB`, `Cargo.toml`, `test_surface` を本体 `catalog_items` に置く。
- `grep` / `change_signal` / `symbols` は catalog_items の fact.type にしない。grep hit は該当 file/symbol item の evidence として吸収する。count のみなら scan_summary へ置く。
- `03_symbols.md 全体`, `30_static_signal_hits.md 全体`, `99_scan_limitations.md 全体` の説明を書かない。それらは repo object を照らす evidence であって subject ではない。
- catalog_items は fact と meaning の対で書く。fact には観測事実だけを書き、推論やリスク含意は meaning.current_implication に置く。
- meaning.role はその項目/ファイルが現在システム内で何であるかを書く。
- meaning.current_implication は現在の含意だけを書く。risk signal は記述的に書いてよいが、何をすべきかは書かない。
- meaning は evidence file を開かずに読める repo 固有の内容にする。「詳細は当該 evidence/インベントリファイルを参照」は禁止。
- `確認が必要` / `確認する必要がある` / `調査が必要` のような次行動要求を書かない。判断に効く未確定の含意は `current_implication` に記述的に書き、判断や追加調査は消費側に残す。
- この禁止は `scan_summary` / `evidence_appendix` にも適用する。appendix も「証拠へのリンク集」ではなく、自己完結した短い要約にする。
- 「TODO は未完了作業を示す」「変更シグナルは最近変更された可能性を示す」「grep hit は静的シグナルである」だけの辞書説明は禁止。
- `domain` は scan profile のコピーではなく、実コード・entrypoint・domain evidence から推定する。YAML/JSON/config があるだけで `infra` にしない。
- `domain: infra` は `domain/00_infra_resources.md` に具体的な infra resource/job/image/env reference がある場合に限定する。`status: no infra domain evidence detected` なら CLI / library / web など主対象の domain を選ぶ。
- `next_action` / `recommended_decision` / `decision_options` / `validation_plan` / `rollback_condition` / `failure_conditions` / `allowed_files` / `max_files_changed` は絶対に書かない。
- grep no-hit を「存在しない」「not found」「absent」と断定しない。低リスク判断でも「検出されていない」ではなく「cited evidence の範囲では小さい/限定的」と書く。
- no-hit に触れる必要がある場合は、必ず「不存在の証明ではない / not proof of absence」と同じ文の中で明記する。
- secret 値を出さない。

Return JSON only. Do not include markdown or review_status.