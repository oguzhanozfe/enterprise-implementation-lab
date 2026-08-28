"""A dependency-free mock activation service used by the UAT examples."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256


VALID_CHANNELS = {"mobile", "web", "branch"}


@dataclass(frozen=True)
class ActivationRequest:
    """Synthetic request contract for a fictional customer activation flow."""

    customer_id: str
    channel: str
    consent: bool
    idempotency_key: str


@dataclass(frozen=True)
class ActivationResult:
    status: str
    activation_id: str | None = None
    error_code: str | None = None


def activate(request: ActivationRequest) -> ActivationResult:
    """Validate a request and return a deterministic synthetic result.

    No data is stored and no external service is called. Deterministic IDs make
    retry and idempotency behavior easy to validate during UAT.
    """

    if not request.customer_id.startswith("SYN-"):
        return ActivationResult(status="rejected", error_code="INVALID_CUSTOMER")
    if request.channel not in VALID_CHANNELS:
        return ActivationResult(status="rejected", error_code="INVALID_CHANNEL")
    if not request.consent:
        return ActivationResult(status="rejected", error_code="CONSENT_REQUIRED")
    if len(request.idempotency_key.strip()) < 8:
        return ActivationResult(status="rejected", error_code="INVALID_IDEMPOTENCY_KEY")

    digest = sha256(
        f"{request.customer_id}:{request.channel}:{request.idempotency_key}".encode("utf-8")
    ).hexdigest()[:12]
    return ActivationResult(status="activated", activation_id=f"ACT-{digest}")
