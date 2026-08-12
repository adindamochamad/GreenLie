#!/usr/bin/env bash
# Generate demo video from docs/VIDEO-SCRIPT.md
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/generate-demo-video.py
echo ""
echo "Preview: open docs/GreenLie-demo.mp4"
open docs/GreenLie-demo.mp4 2>/dev/null || true
