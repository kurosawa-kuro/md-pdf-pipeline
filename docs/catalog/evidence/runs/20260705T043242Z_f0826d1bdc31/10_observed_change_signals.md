# Observed Change Signals

evidence_id: ev.change_signal.summary

This is git history evidence for files that changed often. It is not a defect claim.

| path | commit_count | churn | distinct_authors | last_changed |
|---|---:|---:|---:|---|
| `README.md` | 4 | 182 | 1 | `2026-05-31T20:17:03+09:00` |
| `CLAUDE.md` | 4 | 109 | 1 | `2026-05-31T20:17:03+09:00` |
| `AGENTS.md` | 4 | 104 | 1 | `2026-05-31T20:17:03+09:00` |
| `"doc/02_\347\247\273\350\241\214\343\203\255\343\203\274\343\203\211\343\203\236\343\203\203\343\203\227.md"` | 2 | 242 | 1 | `2026-05-31T20:08:36+09:00` |
| `"doc/01_\344\273\225\346\247\230\343\201\250\350\250\255\350\250\210.md"` | 2 | 198 | 1 | `2026-05-31T20:17:03+09:00` |
| `"doc/03_\345\256\237\350\243\205\343\202\253\343\202\277\343\203\255\343\202\260.md"` | 2 | 176 | 1 | `2026-05-31T20:17:03+09:00` |
| `"doc/04_\351\201\213\347\224\250.md"` | 2 | 136 | 1 | `2026-05-31T20:17:03+09:00` |
| `Makefile` | 2 | 63 | 1 | `2026-05-31T20:17:03+09:00` |
| `src/cli.py` | 1 | 84 | 1 | `2026-05-31T20:17:03+09:00` |
| `.gitignore` | 1 | 79 | 1 | `2026-05-31T16:42:14+09:00` |
| `src/styles/print.css` | 1 | 76 | 1 | `2026-05-31T20:17:03+09:00` |
| `src/pdf_renderer.py` | 1 | 74 | 1 | `2026-05-31T20:17:03+09:00` |
| `doc/README.md` | 1 | 70 | 1 | `2026-05-31T16:42:14+09:00` |
| `doppler.yaml` | 1 | 38 | 1 | `2026-05-31T16:42:14+09:00` |
| `src/html_renderer.py` | 1 | 26 | 1 | `2026-05-31T20:17:03+09:00` |
| `src/examples/sample.md` | 1 | 22 | 1 | `2026-05-31T20:17:03+09:00` |
| `src/markdown_loader.py` | 1 | 21 | 1 | `2026-05-31T20:17:03+09:00` |
| `env/config.yaml` | 1 | 20 | 1 | `2026-05-31T16:42:14+09:00` |
| `src/templates/base.html` | 1 | 10 | 1 | `2026-05-31T20:17:03+09:00` |
| `requirements.txt` | 1 | 2 | 1 | `2026-05-31T20:17:03+09:00` |

## Notes

- churn = added + deleted lines from `git log --numstat`.
- binary file churn is counted as 0 when git reports `-`.
