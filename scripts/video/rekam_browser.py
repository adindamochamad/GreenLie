"""Rekam interaksi browser nyata untuk demo video GreenLie."""

from __future__ import annotations

import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "docs" / "video-build"
URL = "https://web-flax-xi-10.vercel.app"


def rekam_clip(nama: str, aksi) -> Path:
    """Rekam satu clip browser dan return path video."""
    BUILD.mkdir(parents=True, exist_ok=True)
    folder_video = BUILD / "playwright-tmp"
    folder_video.mkdir(exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            color_scheme="dark",
            record_video_dir=str(folder_video),
            record_video_size={"width": 1920, "height": 1080},
        )
        page = context.new_page()
        aksi(page)
        page.wait_for_timeout(800)
        video = page.video
        path_asli = Path(video.path()) if video else None
        context.close()
        browser.close()

    if path_asli and path_asli.exists():
        tujuan = BUILD / f"{nama}.webm"
        path_asli.rename(tujuan)
        return tujuan

    raise FileNotFoundError(f"Gagal rekam clip {nama}")


def aksi_hero(page):
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(2500)


def aksi_ao(page):
    page.goto(f"{URL}/#built-with-ao", wait_until="networkidle")
    page.wait_for_timeout(500)
    page.locator("#built-with-ao").scroll_into_view_if_needed()
    page.wait_for_timeout(4500)


def aksi_demo(page):
    page.goto(f"{URL}/#demo", wait_until="networkidle")
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Naive merge").click()
    page.wait_for_timeout(2500)
    page.get_by_role("button", name="GreenLie block").click()
    page.wait_for_timeout(4000)


def aksi_tryit(page):
    page.goto(f"{URL}/#try", wait_until="networkidle")
    page.wait_for_timeout(1200)
    page.get_by_role("button", name="greenlie analyze").click()
    page.wait_for_timeout(5000)


def main() -> None:
    print("→ Rekam hero...")
    rekam_clip("03-hero-rec", aksi_hero)
    print("→ Rekam AO section...")
    rekam_clip("02-ao-rec", aksi_ao)
    print("→ Rekam demo toggle...")
    rekam_clip("04-demo-rec", aksi_demo)
    print("→ Rekam Try It...")
    rekam_clip("05-tryit-rec", aksi_tryit)
    print("✓ Browser clips selesai")


if __name__ == "__main__":
    main()
