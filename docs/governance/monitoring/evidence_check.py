#!/usr/bin/env python3
"""Check whether a report includes commit evidence URL.

Usage:
  python3 docs/governance/monitoring/evidence_check.py --file docs/task/attendant.md

Exit codes:
  0: pass
  2: missing evidence
  3: input error
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

COMMIT_URL_RE = re.compile(
    r"https?://github\.com/[\w.-]+/[\w.-]+/(?:commit|pull)/[A-Za-z0-9._-]+"
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, help="Target markdown/text file")
    args = ap.parse_args()

    p = Path(args.file)
    if not p.exists():
        print(f"FAIL: file not found: {p}")
        return 3

    text = p.read_text(encoding="utf-8", errors="ignore")
    matches = COMMIT_URL_RE.findall(text)
    if not matches:
        print("FAIL: commit/pr evidence URL not found")
        return 2

    print("PASS: evidence URL found")
    for m in matches[:5]:
        print(f"- {m}")
    if len(matches) > 5:
        print(f"... and {len(matches) - 5} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
