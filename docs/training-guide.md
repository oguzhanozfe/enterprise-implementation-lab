# Five-minute operator guide

1. Use only the sample cases in `data/uat_cases.json`.
2. Run `python3 scripts/run_uat.py` from the repository root.
3. Read `summary.failed` first; a non-zero value blocks the fictional rollout.
4. Use `case_id` and `requirement_id` to route a defect to the right owner.
5. Never replace synthetic identifiers with real customer data.

This guide demonstrates the handoff layer around code: a repeatable check,
clear escalation boundary, and explicit data-safety rule.
