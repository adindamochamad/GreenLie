#!/usr/bin/env bash
# Salin template submission ke clipboard (macOS pbcopy)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FILE="$ROOT/docs/TIER-D-READY.md"

echo "GreenLie — Tier D clipboard helper"
echo ""
echo "1) discord   — Discord showcase post"
echo "2) x1-x5     — X thread tweets"
echo "3) linkedin  — LinkedIn post"
echo "4) general   — Discord #orchestra-general"
echo "5) open      — Buka semua link submission"
echo ""
read -r -p "Pilih [1-5]: " PILIH

case "$PILIH" in
  1)
    awk '/^Hey everyone!/,/^Feedback welcome/' "$ROOT/docs/SOCIAL-CAPTIONS.md" | pbcopy
    echo "✓ Discord post (descriptive) copied. Paste di #orchestra-project-showcase"
    open "https://discord.gg/87NPrAuDa"
    ;;
  3)
    sed -n '/^```$/,/^```$/p' "$FILE" | sed '1d;$d' | tail -n +12 | head -20 | pbcopy 2>/dev/null || true
    # LinkedIn block is outside code fence — extract manually
    awk '/^## Step 4 — LinkedIn/,/^---$/' "$FILE" | grep -v '^##' | grep -v '^---' | pbcopy
    echo "✓ LinkedIn post copied."
    open "https://www.linkedin.com/feed/"
    ;;
  4)
    awk '/^## Step 5 — Discord/,/^---$/' "$FILE" | grep -v '^##' | grep -v '^---' | grep -v '^```' | pbcopy
    echo "✓ #orchestra-general post copied."
    open "https://discord.gg/87NPrAuDa"
    ;;
  5)
    open "https://web-flax-xi-10.vercel.app"
    open "https://github.com/adindamochamad/GreenLie"
    open "https://discord.gg/87NPrAuDa"
    open "$FILE"
    echo "✓ Opened demo, GitHub, Discord, TIER-D-READY.md"
    ;;
  *)
    echo "X thread: copy manual dari docs/TIER-D-READY.md (Tweet 1/5 – 5/5)"
    open "$FILE"
    ;;
esac

echo ""
echo "Jangan lupa isi [VIDEO_URL] setelah upload video!"
