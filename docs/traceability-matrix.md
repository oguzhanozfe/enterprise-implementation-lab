# Requirements traceability matrix

| Requirement | Design / code | UAT evidence | Rollout gate |
|---|---|---|---|
| REQ-001 — supported channels | `VALID_CHANNELS` in `service.py` | UAT-001, UAT-002 | All supported-channel checks pass |
| REQ-002 — synthetic IDs only | `customer_id.startswith("SYN-")` | UAT-003 | No non-synthetic fixture is accepted |
| REQ-003 — explicit consent | consent validation in `activate` | UAT-004 | Consent-negative path is verified |
| REQ-004 — retry safety | deterministic SHA-256 activation ID | UAT-005, UAT-006 plus unit test | Retry test passes; invalid keys reject |
| REQ-005 — traceable reporting | `uat.py` report schema | Full suite | JSON report has zero failures |

This matrix is intentionally compact. A real implementation would also link
risks, owners, versioned approvals, defects, environments, and production
monitoring evidence.
