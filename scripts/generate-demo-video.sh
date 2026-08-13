#!/usr/bin/env bash
# Generate GreenLie demo video (AO screenshot asli + browser + terminal + TTS)
set -euo pipefail
cd "$(dirname "$0")/.."

for cmd in ffmpeg ffprobe vhs python3; do
  command -v "$cmd" >/dev/null || { echo "Missing: $cmd"; exit 1; }
done

if ! python3 -c "import edge_tts, PIL" 2>/dev/null; then
  pip3 install -r scripts/video/requirements.txt
fi
if ! python3 -c "import playwright" 2>/dev/null; then
  pip3 install playwright && python3 -m playwright install chromium
fi

python3 scripts/generate-demo-video-final.py
echo ""
echo "Preview: open docs/GreenLie-demo.mp4"
open docs/GreenLie-demo.mp4 2>/dev/null || true
