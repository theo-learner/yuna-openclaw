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

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TARGETS_FILE = ROOT / "docs/governance/monitoring/governance_guard_targets.json"


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = "\n".join([s for s in [p.stdout.strip(), p.stderr.strip()] if s]).strip()
    return p.returncode, out


def load_targets() -> tuple[Path, list[Path]]:
    if not TARGETS_FILE.exists():
        raise FileNotFoundError(f"targets file not found: {TARGETS_FILE}")

    data = json.loads(TARGETS_FILE.read_text(encoding="utf-8"))
    gate_rel = data.get("gate")
    evidence_rel = data.get("evidenceTargets", [])

    if not gate_rel or not isinstance(gate_rel, str):
        raise ValueError("invalid targets: 'gate' is required")
    if not isinstance(evidence_rel, list) or not all(isinstance(x, str) for x in evidence_rel):
        raise ValueError("invalid targets: 'evidenceTargets' must be string[]")

    gate = ROOT / gate_rel
    evidence = [ROOT / p for p in evidence_rel]
    return gate, evidence


def main() -> int:
    findings: list[str] = []

    try:
        gate, evidence_targets = load_targets()
    except Exception as e:
        print("RUNTIME_ERROR: failed to load guard targets")
        print(str(e))
        return 3

    # 1) Gate check (bridge: blocked treated as state, not runtime error)
    rc, out = run([
        "python3",
        str(ROOT / "docs/governance/monitoring/gate_precheck_bridge.py"),
        "--gate",
        str(gate),
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
    for target in evidence_targets:
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
