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
