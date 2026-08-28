# Rollout runbook

## Before rollout

1. Freeze the candidate commit and record its SHA.
2. Run unit tests and the documented UAT suite.
3. Confirm training notes and support ownership.
4. Review open risks, dependencies, rollback owner, and decision maker.

## Fictional phased release

1. Internal test cohort.
2. Five-percent synthetic traffic replay.
3. Twenty-five-percent synthetic traffic replay.
4. Full synthetic load only after agreed error and latency gates hold.

## Stop conditions

- Any acceptance regression.
- Duplicate activation IDs for different idempotency keys.
- A non-synthetic identifier is accepted.
- Ownership or rollback path is unclear.

## Rollback

Disable the candidate route, restore the previous tagged version, retain test
evidence, and open a decision record before retrying.
