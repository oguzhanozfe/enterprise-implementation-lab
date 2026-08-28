#!/usr/bin/env python3
"""Run the synthetic UAT suite and emit a machine-readable report."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from implementation_lab.uat import report, run_suite  # noqa: E402


def main() -> int:
    results = run_suite(ROOT / "data" / "uat_cases.json")
    payload = report(results)
    print(json.dumps(payload, indent=2))
    return 0 if payload["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
