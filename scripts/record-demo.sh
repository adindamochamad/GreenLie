#!/usr/bin/env bash
# Helper: buka semua app yang perlu direkam untuk demo video Tier B
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
URL_DEMO="https://web-flax-xi-10.vercel.app"

echo "🎬 GreenLie — Recording prep"
echo ""
echo "1. Start screen recorder (QuickTime / OBS / Loom)"
echo "2. Follow docs/VIDEO-SELF-SCRIPT.md (detail scene + script)"
echo ""
read -r -p "Press Enter when recorder is running..."

echo "→ Opening live demo..."
open "$URL_DEMO"

echo "→ Opening Agent Orchestrator..."
open -a "Agent Orchestrator" 2>/dev/null || echo "   (Install AO or open manually)"

echo "→ Opening GitHub repo..."
open "https://github.com/adindamochamad/GreenLie"

echo ""
echo "When ready for terminal shot, run:"
echo "  cd $ROOT && ./scripts/demo.sh"
echo ""
echo "After upload video → fill [VIDEO_URL] in docs/TIER-D-READY.md"
echo "Then post Discord + X + LinkedIn from that file."
