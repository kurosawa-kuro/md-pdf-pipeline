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
