# UAT plan

## Objective

Demonstrate that the documented happy paths and rejection paths behave as
agreed before a fictional rollout decision.

## Entry criteria

- Requirements and traceability matrix reviewed.
- Unit tests pass on the candidate commit.
- Test data contains only `SYN-` identifiers.

## Execution

```bash
python3 scripts/run_uat.py
```

## Exit criteria

- Six of six documented UAT cases pass.
- No case is missing a requirement ID.
- The report process exits with status code `0`.

## Defect handling

A failed case blocks the rollout gate. Record the case, requirement, actual
result, owner, severity, proposed fix, and retest evidence before reconsidering
the decision.
