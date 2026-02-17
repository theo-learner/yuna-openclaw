#!/usr/bin/env python3
"""Local-only governance guard audit (no cron API calls).

Outputs one of:
- LOCAL_GUARD_OK
- LOCAL_GUARD_FINDINGS + lines
- RUNTIME_ERROR + reason
"""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REQUIRED_FILES = [
    ROOT / "docs/governance/monitoring/run_guarded_action.sh",
    ROOT / "docs/governance/monitoring/gate_precheck.py",
    ROOT / "docs/governance/monitoring/evidence_check.py",
    ROOT / "docs/governance/monitoring/governance_guard_runner.py",
    ROOT / "docs/governance/monitoring/governance_guard_targets.json",
]


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = "\n".join([s for s in [p.stdout.strip(), p.stderr.strip()] if s]).strip()
    return p.returncode, out


def main() -> int:
    findings: list[str] = []

    for p in REQUIRED_FILES:
        if not p.exists():
            findings.append(f"MISSING_FILE: {p.relative_to(ROOT)}")

    wrapper = ROOT / "docs/governance/monitoring/run_guarded_action.sh"
    if wrapper.exists():
        mode = wrapper.stat().st_mode
        if not (mode & stat.S_IXUSR):
            findings.append("WRAPPER_NOT_EXECUTABLE: docs/governance/monitoring/run_guarded_action.sh")

    rc, out = run(["python3", str(ROOT / "docs/governance/monitoring/governance_guard_runner.py")])
    if rc != 0:
        print("RUNTIME_ERROR: governance_guard_runner execution failed")
        if out:
            print(out)
        return 3

    if "GUARD_FINDINGS" in out:
        findings.append("RUNNER_FINDINGS_PRESENT")
    elif "GUARD_OK" not in out:
        findings.append("RUNNER_OUTPUT_UNKNOWN")

    if not findings:
        print("LOCAL_GUARD_OK")
        return 0

    print("LOCAL_GUARD_FINDINGS")
    for f in findings:
        print(f"- {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
