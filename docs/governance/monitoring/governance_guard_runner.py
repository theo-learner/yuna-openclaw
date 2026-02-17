#!/usr/bin/env python3
"""Unified governance guard runner.

Checks:
1) CEO gate status
2) Evidence URL presence in selected governance docs

Exit policy (cron-friendly):
- always 0 for PASS/BLOCKED/FAIL_FINDING (operational finding)
- non-zero only for execution/runtime errors
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GATE = ROOT / "docs/business/feature/gajae-bip-service/pm/GATE.md"
EVIDENCE_TARGETS = [
    ROOT / "docs/business/feature/gajae-bip-service/pm/GATE.md",
    ROOT / "docs/task/attendant.md",
]


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = "\n".join([s for s in [p.stdout.strip(), p.stderr.strip()] if s]).strip()
    return p.returncode, out


def main() -> int:
    findings: list[str] = []

    # 1) Gate check (bridge: blocked treated as state, not runtime error)
    rc, out = run([
        "python3",
        str(ROOT / "docs/governance/monitoring/gate_precheck_bridge.py"),
        "--gate",
        str(GATE),
    ])
    if rc != 0:
        print("RUNTIME_ERROR: gate bridge execution failed")
        if out:
            print(out)
        return 3

    if "BLOCKED_STATE" in out:
        findings.append("GATE_BLOCKED: CEO approval waiting")
    elif "PASS:" in out:
        pass
    else:
        findings.append("GATE_UNKNOWN: unexpected gate output")

    # 2) Evidence checks
    for target in EVIDENCE_TARGETS:
        rc, out = run([
            "python3",
            str(ROOT / "docs/governance/monitoring/evidence_check.py"),
            "--file",
            str(target),
        ])
        if rc == 0:
            continue
        if rc in (2, 3):
            findings.append(f"EVIDENCE_FAIL: {target.relative_to(ROOT)}")
        else:
            print("RUNTIME_ERROR: evidence check execution failed")
            if out:
                print(out)
            return 3

    if not findings:
        print("GUARD_OK")
        return 0

    print("GUARD_FINDINGS")
    for f in findings:
        print(f"- {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
