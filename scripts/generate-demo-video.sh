#!/usr/bin/env bash
# Generate pro demo video (browser recording + VHS terminal + neural TTS)
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v vhs >/dev/null; then
  echo "Install: brew install vhs"
  exit 1
fi
if ! python3 -c "import edge_tts, playwright" 2>/dev/null; then
  echo "Install: pip install edge-tts playwright && python3 -m playwright install chromium"
  exit 1
fi

python3 scripts/generate-demo-video-pro.py
echo ""
echo "Preview: open docs/GreenLie-demo.mp4"
open docs/GreenLie-demo.mp4 2>/dev/null || true
