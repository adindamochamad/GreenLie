#!/usr/bin/env bash
# Buka YouTube Studio upload + copy metadata ke clipboard (macOS)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOC="$ROOT/docs/YOUTUBE-UPLOAD.md"

echo "GreenLie — YouTube upload helper"
echo ""

# Title (baris setelah ``` di section Title recommended)
TITLE='GreenLie — Catch When AI "Fixes" Tests Instead of Bugs | Agent Orchestrator Hackathon #agentorchestrator'

case "${1:-menu}" in
  title)
    echo -n "$TITLE" | pbcopy
    echo "✓ Title copied to clipboard"
    ;;
  desc)
    sed -n '/^GreenLie — demo for The Orchestra/,/^Timestamps/p' "$DOC" | sed '$d' | pbcopy
    echo "✓ Description copied to clipboard"
    ;;
  tags)
    echo -n "agent orchestrator, agentorchestrator, the orchestra hackathon, greenlie, aoagents, ai coding agents, devtools, ci cd, software testing, hackathon demo" | pbcopy
    echo "✓ Tags copied to clipboard"
    ;;
  open)
    open "https://studio.youtube.com/channel/UC/videos?d=ud"
    open "$DOC"
    echo "✓ YouTube Studio + YOUTUBE-UPLOAD.md opened"
    echo "  Run: $0 title | desc | tags  to copy metadata"
    ;;
  *)
    echo "Usage:"
    echo "  $0 open   — YouTube Studio + docs"
    echo "  $0 title  — copy title"
    echo "  $0 desc   — copy description"
    echo "  $0 tags   — copy tags"
    echo ""
    echo "Full guide: docs/YOUTUBE-UPLOAD.md"
    ;;
esac
