# Decision log

## ADR-001 — use a dependency-free local service

**Decision:** Use Python standard-library code with no network or persistence.

**Why:** The portfolio goal is to make requirements, acceptance behavior, UAT,
and rollout reasoning inspectable without presenting a toy service as a
production banking platform.

**Trade-off:** This does not demonstrate authentication, observability,
distributed systems, or regulatory controls. Those remain explicit non-goals.

## ADR-002 — deterministic activation IDs

**Decision:** Derive a short synthetic activation ID from customer, channel,
and idempotency key.

**Why:** Retry behavior becomes testable without storing state.

**Trade-off:** A production design would require stronger domain, security,
collision, audit, and privacy analysis.
