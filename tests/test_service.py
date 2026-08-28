from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from implementation_lab.service import ActivationRequest, activate  # noqa: E402
from implementation_lab.uat import report, run_suite  # noqa: E402


class ActivationServiceTests(unittest.TestCase):
    def test_valid_request_is_activated(self) -> None:
        result = activate(ActivationRequest("SYN-100", "mobile", True, "retry-key-100"))
        self.assertEqual(result.status, "activated")
        self.assertTrue(result.activation_id and result.activation_id.startswith("ACT-"))

    def test_same_request_is_idempotent(self) -> None:
        request = ActivationRequest("SYN-101", "web", True, "retry-key-101")
        self.assertEqual(activate(request), activate(request))

    def test_consent_is_required(self) -> None:
        result = activate(ActivationRequest("SYN-102", "branch", False, "retry-key-102"))
        self.assertEqual(result.error_code, "CONSENT_REQUIRED")

    def test_unknown_channel_is_rejected(self) -> None:
        result = activate(ActivationRequest("SYN-103", "partner", True, "retry-key-103"))
        self.assertEqual(result.error_code, "INVALID_CHANNEL")

    def test_documented_uat_suite_passes(self) -> None:
        payload = report(run_suite(ROOT / "data" / "uat_cases.json"))
        self.assertEqual(payload["summary"]["failed"], 0)
        self.assertEqual(payload["summary"]["passed"], 6)


if __name__ == "__main__":
    unittest.main()
