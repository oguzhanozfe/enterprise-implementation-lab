# Requirements brief

## Fictional business context

A fictional financial-services team is adding a small activation service to its
mobile, web, and branch journeys. Business, engineering, QA, training, and
rollout owners need one shared acceptance boundary.

## Scope

- Accept only synthetic identifiers and three documented channels.
- Require consent and retry-safe idempotency keys.
- Keep the reference implementation stateless and dependency-free.
- Map every UAT case to a requirement.

## Out of scope

- Identity verification, authentication, payments, balances, or personal data.
- Production security, persistence, observability, or regulatory compliance.
- Any connection to a real bank, customer, or vendor system.

The machine-readable source of truth is [`data/requirements.json`](../data/requirements.json).
