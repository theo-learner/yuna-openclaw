#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash docs/governance/monitoring/run_guarded_action.sh \
#     --gate docs/business/feature/gajae-bip-service/pm/GATE.md \
#     --evidence docs/task/attendant.md \
#     -- <actual command>

GATE_PATH=""
EVIDENCE_PATH=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --gate)
      GATE_PATH="$2"; shift 2 ;;
    --evidence)
      EVIDENCE_PATH="$2"; shift 2 ;;
    --)
      shift
      break ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 3 ;;
  esac
done

if [[ -z "${GATE_PATH}" || -z "${EVIDENCE_PATH}" ]]; then
  echo "Usage: $0 --gate <GATE.md> --evidence <REPORT.md> -- <actual command>" >&2
  exit 3
fi

if [[ $# -eq 0 ]]; then
  echo "No action command provided after --" >&2
  exit 3
fi

python3 docs/governance/monitoring/gate_precheck.py --gate "${GATE_PATH}"
python3 docs/governance/monitoring/evidence_check.py --file "${EVIDENCE_PATH}"

echo "PASS: guarded checks passed. executing action..."
"$@"
