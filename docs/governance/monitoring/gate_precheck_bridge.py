#!/usr/bin/env python3
"""Bridge wrapper for cron-safe gate checks.

- PASS -> exit 0
- BLOCKED(approval waiting) -> exit 0 with blocked message
- Unexpected error -> exit 3
"""

from __future__ import annotations

import argparse
import subprocess
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", required=True)
    args = ap.parse_args()

    cmd = [
        "python3",
        "docs/governance/monitoring/gate_precheck.py",
        "--gate",
        args.gate,
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    merged = "\n".join([s for s in [out, err] if s]).strip()

    if proc.returncode == 0:
        print("PASS: gate check passed")
        return 0

    if proc.returncode == 2:
        print("BLOCKED_STATE: CEO approval waiting")
        if merged:
            print(merged)
        return 0

    print("ERROR: gate check execution failed")
    if merged:
        print(merged)
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
