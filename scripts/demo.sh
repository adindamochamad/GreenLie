#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/engine"

echo "? Installing GreenLie engine..."
python3 -m venv .venv
source .venv/bin/activate
pip install -q -e ".[dev]"

echo ""
echo "? Running GreenLie analyze on sample..."
greenlie analyze --format table

echo ""
echo "? JSON output:"
greenlie analyze --format json
