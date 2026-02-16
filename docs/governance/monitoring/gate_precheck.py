#!/usr/bin/env python3
"""Pre-action gate checker for CEO approval gate files.

Usage:
  python3 docs/governance/monitoring/gate_precheck.py \
    --gate docs/business/feature/gajae-bip-service/pm/GATE.md

Exit codes:
  0: pass (safe to proceed)
  2: blocked by approval gate
  3: parse/input error
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

WAITING_TOKENS = ("WAITING", "⏳", "대기", "미승인")
ACTIVE_TOKENS = ("INPROGRESS", "IN_PROGRESS", "진행")


def parse_rows(md: str):
    rows = []
    for line in md.splitlines():
        if not line.strip().startswith("|"):
            continue
        if ":---" in line:
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 7:
            continue
        # Skip header row
        if "피쳐명" in cols[0] and "CEO 승인" in cols[4]:
            continue
        rows.append(
            {
                "feature": cols[0],
                "step": cols[1],
                "owner": cols[2],
                "status": cols[3],
                "ceo": cols[4],
                "updated": cols[5],
                "evidence": cols[6],
            }
        )
    return rows


def has_token(text: str, tokens: tuple[str, ...]) -> bool:
    u = re.sub(r"\*|`|\[|\]|\(|\)", "", text).upper()
    return any(t.upper() in u for t in tokens)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", required=True, help="Path to GATE.md")
    args = ap.parse_args()

    p = Path(args.gate)
    if not p.exists():
        print(f"BLOCKED: gate file not found: {p}")
        return 3

    content = p.read_text(encoding="utf-8")
    rows = parse_rows(content)
    if not rows:
        print("BLOCKED: no gate rows parsed")
        return 3

    blockers = []
    for r in rows:
        in_progress = has_token(r["status"], ACTIVE_TOKENS)
        waiting = has_token(r["ceo"], WAITING_TOKENS) or not r["ceo"].strip()
        if in_progress and waiting:
            blockers.append(r)

    if blockers:
        print("BLOCKED: CEO approval gate not satisfied")
        for b in blockers:
            print(
                f"- {b['feature']} | {b['step']} | status={b['status']} | ceo={b['ceo']}"
            )
        return 2

    print("PASS: CEO gate check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
