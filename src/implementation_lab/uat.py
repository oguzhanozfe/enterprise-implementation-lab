"""Execute traceable UAT cases against the synthetic service."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .service import ActivationRequest, activate


@dataclass(frozen=True)
class UatResult:
    case_id: str
    requirement_id: str
    passed: bool
    expected_status: str
    actual_status: str
    expected_error: str | None
    actual_error: str | None


def load_cases(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("UAT file must contain a list of cases")
    return payload


def run_case(case: dict[str, Any]) -> UatResult:
    request = ActivationRequest(**case["request"])
    actual = activate(request)
    expected_error = case.get("expected_error")
    passed = actual.status == case["expected_status"] and actual.error_code == expected_error
    return UatResult(
        case_id=case["case_id"],
        requirement_id=case["requirement_id"],
        passed=passed,
        expected_status=case["expected_status"],
        actual_status=actual.status,
        expected_error=expected_error,
        actual_error=actual.error_code,
    )


def run_suite(path: Path) -> list[UatResult]:
    return [run_case(case) for case in load_cases(path)]


def report(results: list[UatResult]) -> dict[str, Any]:
    return {
        "summary": {
            "total": len(results),
            "passed": sum(result.passed for result in results),
            "failed": sum(not result.passed for result in results),
        },
        "results": [asdict(result) for result in results],
    }
