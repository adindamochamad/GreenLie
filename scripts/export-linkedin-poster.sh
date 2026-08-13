#!/usr/bin/env bash
# Export linkedin-poster.html → PNG 1920×1080
set -euo pipefail
cd "$(dirname "$0")/.."

HTML="docs/assets/linkedin-poster.html"
OUT="docs/assets/linkedin-poster.png"

if ! python3 -c "import playwright" 2>/dev/null; then
  echo "Install: pip install playwright && python3 -m playwright install chromium"
  exit 1
fi

python3 <<'PY'
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(".")
html = (root / "docs/assets/linkedin-poster.html").resolve().as_uri()
out = root / "docs/assets/linkedin-poster.png"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    page.goto(html)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1500)  # tunggu Google Fonts
    page.screenshot(path=str(out), type="png")
    browser.close()

print(f"✓ Exported: {out}")
PY

open "$OUT" 2>/dev/null || true
