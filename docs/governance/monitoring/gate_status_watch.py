#!/usr/bin/env python3
"""Detect gate status transitions and emit only on change.

State file default:
  /home/theo/.openclaw/workspace/memory/gajae-gate-transition-state.json
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, UTC
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GATE = ROOT / "docs/business/feature/gajae-bip-service/pm/GATE.md"
STATE_FILE = Path("/home/theo/.openclaw/workspace/memory/gajae-gate-transition-state.json")


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = "\n".join([s for s in [p.stdout.strip(), p.stderr.strip()] if s]).strip()
    return p.returncode, out


def current_status() -> tuple[str, str]:
    rc, out = run([
        "python3",
        str(ROOT / "docs/governance/monitoring/gate_precheck_bridge.py"),
        "--gate",
        str(GATE),
    ])
    if rc != 0:
        return "ERROR", out
    if "BLOCKED_STATE" in out:
        return "BLOCKED", out
    if "PASS:" in out:
        return "PASS", out
    return "UNKNOWN", out


def load_prev() -> str | None:
    if not STATE_FILE.exists():
        return None
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        return data.get("status")
    except Exception:
        return None


def save(status: str) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps({"status": status, "updatedAt": datetime.now(UTC).isoformat()}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    status, detail = current_status()
    if status == "ERROR":
        print("RUNTIME_ERROR")
        print(detail)
        return 3

    prev = load_prev()
    save(status)

    if prev is None:
        print("INITIAL_STATE")
        print(f"- status: {status}")
        return 0

    if prev == status:
        print("NO_CHANGE")
        return 0

    print("STATE_CHANGED")
    print(f"- previous: {prev}")
    print(f"- current: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
