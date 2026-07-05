# Static Signal Hits

This is a machine-generated signal inventory, not a decision.
Every row points back to grep evidence.

| query_id | hit_state | hits | evidence_ref | follow_up |
|---|---|---:|---|---|
| `todos` | `no_hit` | 0 | `file=evidence/grep/01_todos.md query_id=todos` | treat as no-hit, not absence |
| `job_lifecycle` | `matched` | 1 | `file=evidence/grep/02_job_lifecycle.md query_id=job_lifecycle` | review matching lines before deciding |
| `env_secret` | `matched` | 6 | `file=evidence/grep/03_env_secret.md query_id=env_secret` | review matching lines before deciding |
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
