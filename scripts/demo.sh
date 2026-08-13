#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/engine"

echo "-- Installing GreenLie engine..."
python3 -m venv .venv >/dev/null
source .venv/bin/activate
pip install -q -e ".[dev]"

echo ""
echo "== Scenario 1: naive auth CI-fix (default sample) =="
greenlie analyze --format table || true

echo ""
echo "== Scenario 2: ORM query assertions weakened =="
greenlie analyze \
  --before "$ROOT/samples/extra/orm-query/before-agent-fix" \
  --after  "$ROOT/samples/extra/orm-query/after-agent-fix" \
  --format table || true

echo ""
echo "== Scenario 3: Exception assertions weakened =="
greenlie analyze \
  --before "$ROOT/samples/extra/error-throw/before-agent-fix" \
  --after  "$ROOT/samples/extra/error-throw/after-agent-fix" \
  --format table || true

echo ""
echo "-- JSON output for default sample:"
greenlie analyze --format json
