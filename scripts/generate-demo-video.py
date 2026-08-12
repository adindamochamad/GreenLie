#!/usr/bin/env python3
"""Generate GreenLie demo video from script using ffmpeg + macOS TTS."""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "docs" / "video-build"
OUTPUT = ROOT / "docs" / "GreenLie-demo.mp4"

LEBAR = 1920
TINGGI = 1080
FPS = 25
BG = (13, 15, 12)
HIJAU = (61, 255, 122)
MERAH = (255, 59, 48)
TEKS = (232, 228, 220)
ABU = (138, 143, 130)
ORanye = (196, 77, 46)

SEGmen = [
    {
        "id": "01-hook",
        "durasi_min": 12,
        "gambar": None,
        "teks_gambar": [
            ("GreenLie", 96, HIJAU, 120),
            ("CI passed. Auth was broken.", 52, TEKS, 420),
            ("The agent didn't fix the bug —", 40, ABU, 520),
            ("it fixed the test.", 40, MERAH, 580),
        ],
        "narasi": "CI passed. Auth was broken. The agent didn't fix the bug — it fixed the test.",
    },
    {
        "id": "02-ao",
        "durasi_min": 30,
        "gambar": BUILD / "02-ao-kanban.png",
        "narasi": "GreenLie was built with Agent Orchestrator — parallel agents on engine, API, and demo site.",
    },
    {
        "id": "03-hero",
        "durasi_min": 22,
        "gambar": BUILD / "01-hero.png",
        "narasi": "Same agent fix. Two outcomes. Naive merge — board green, CI pass.",
    },
    {
        "id": "04-demo",
        "durasi_min": 14,
        "gambar": BUILD / "03-demo.png",
        "narasi": "GreenLie: integrity 29 percent. Five critical findings. Merge blocked.",
    },
    {
        "id": "05-tryit",
        "durasi_min": 18,
        "gambar": BUILD / "04-tryit.png",
        "narasi": "Live API scan — same engine, same sample.",
    },
    {
        "id": "06-terminal",
        "durasi_min": 18,
        "gambar": BUILD / "05-terminal.png",
        "narasi": "CLI: GL-001 — toBe(401) became toBeGreaterThan(0). Status 500 also passes.",
    },
    {
        "id": "07-github",
        "durasi_min": 16,
        "gambar": BUILD / "06-split.png",
        "narasi": "Open source. Built for The Orchestra hackathon.",
    },
    {
        "id": "08-end",
        "durasi_min": 12,
        "gambar": None,
        "teks_gambar": [
            ("GreenLie", 88, ORanye, 280),
            ("web-flax-xi-10.vercel.app", 36, TEKS, 420),
            ("github.com/adindamochamad/GreenLie", 32, ABU, 490),
            ("#agentorchestrator · Built with Agent Orchestrator", 28, HIJAU, 560),
            ("CI passed. Tests lied.", 44, MERAH, 680),
        ],
        "narasi": "Try it at web-flax-xi-10.vercel.app. GreenLie — CI passed. Tests lied.",
    },
]


def jalankan(perintah: list[str], *, check: bool = True) -> subprocess.CompletedProcess:
    """Jalankan subprocess dan tampilkan error jika gagal."""
    print("→", " ".join(perintah[:6]), "..." if len(perintah) > 6 else "")
    return subprocess.run(perintah, check=check, capture_output=True, text=True)


def cari_font(ukuran: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Cari font monospace/sans yang tersedia di macOS."""
    kandidat = [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Supplemental/Andale Mono.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for jalur in kandidat:
        if Path(jalur).exists():
            try:
                return ImageFont.truetype(jalur, ukuran)
            except OSError:
                continue
    return ImageFont.load_default()


def buat_slide_teks(segmen: dict) -> Path:
    """Render slide teks untuk hook / end card."""
    img = Image.new("RGB", (LEBAR, TINGGI), BG)
    draw = ImageDraw.Draw(img)
    for teks, ukuran, warna, y in segmen.get("teks_gambar", []):
        font = cari_font(ukuran)
        draw.text((LEBAR // 2, y), teks, fill=warna, font=font, anchor="mm")
    jalur = BUILD / f"{segmen['id']}-slide.png"
    img.save(jalur)
    return jalur


def buat_slide_terminal() -> Path:
    """Render output demo.sh sebagai slide terminal."""
    sumber = BUILD / "terminal-output.txt"
    if not sumber.exists():
        jalankan(["bash", str(ROOT / "scripts" / "demo.sh")], check=False)
        # demo.sh exit 1 expected — capture stdout separately
        subprocess.run(
            f"cd {ROOT} && ./scripts/demo.sh 2>/dev/null | head -35",
            shell=True,
            stdout=open(sumber, "w"),
            text=True,
        )

    isi = sumber.read_text(encoding="utf-8") if sumber.exists() else "GreenLie analyze output"
    img = Image.new("RGB", (LEBAR, TINGGI), (28, 33, 24))
    draw = ImageDraw.Draw(img)
    font = cari_font(22)
    font_besar = cari_font(28)

    draw.text((80, 60), "$ ./scripts/demo.sh", fill=HIJAU, font=font_besar)
    y = 130
    for baris in isi.splitlines()[:28]:
        warna = TEKS
        if "CRITICAL" in baris or "GL-001" in baris:
            warna = MERAH
        elif "Integrity" in baris:
            warna = HIJAU
        draw.text((80, y), baris[:100], fill=warna, font=font)
        y += 32

    jalur = BUILD / "05-terminal.png"
    img.save(jalur)
    return jalur


def buat_slide_split() -> Path:
    """Composite AO kanban + GitHub label untuk segment split."""
    ao = Image.open(BUILD / "02-ao-kanban.png").convert("RGB")
    img = Image.new("RGB", (LEBAR, TINGGI), BG)
    ao_resized = ao.resize((LEBAR // 2 - 40, TINGGI - 80))
    img.paste(ao_resized, (40, 40))

    draw = ImageDraw.Draw(img)
    font = cari_font(36)
    font_kecil = cari_font(26)
    x = LEBAR // 2 + 20
    draw.text((x, 200), "Open Source", fill=TEKS, font=font)
    draw.text((x, 280), "github.com/adindamochamad", fill=ABU, font=font_kecil)
    draw.text((x, 330), "/GreenLie", fill=HIJAU, font=font_kecil)
    draw.text((x, 420), "The Orchestra 2026", fill=ORanye, font=font)
    draw.text((x, 500), "Engine · API · Demo", fill=ABU, font=font_kecil)
    draw.text((x, 560), "Built with Agent Orchestrator", fill=TEKS, font=font_kecil)

    jalur = BUILD / "06-split.png"
    img.save(jalur)
    return jalur


def buat_narasi(segmen: dict) -> tuple[Path, float]:
    """Generate TTS audio via macOS say."""
    aiff = BUILD / f"{segmen['id']}.aiff"
    m4a = BUILD / f"{segmen['id']}.m4a"
    jalankan(["say", "-v", "Samantha", "-r", "175", "-o", str(aiff), segmen["narasi"]])
    jalankan(["ffmpeg", "-y", "-i", str(aiff), "-c:a", "aac", "-b:a", "192k", str(m4a)])
    probe = jalankan(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(m4a),
        ]
    )
    durasi = max(float(probe.stdout.strip()), segmen["durasi_min"])
    return m4a, durasi


def buat_clip_video(gambar: Path, audio: Path, durasi: float, keluaran: Path) -> None:
    """Convert static image + audio to video clip with subtle zoom."""
    total_frame = int(durasi * FPS)
    filter_zoom = (
        f"scale={LEBAR}:{TINGGI}:force_original_aspect_ratio=decrease,"
        f"pad={LEBAR}:{TINGGI}:(ow-iw)/2:(oh-ih)/2:color=0x0D0F0C,"
        f"zoompan=z='min(zoom+0.0008,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"d={total_frame}:s={LEBAR}x{TINGGI}:fps={FPS}"
    )
    jalankan(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(gambar),
            "-i",
            str(audio),
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-pix_fmt",
            "yuv420p",
            "-t",
            str(durasi),
            "-vf",
            filter_zoom,
            str(keluaran),
        ]
    )


def gabung_clips(clips: list[Path], keluaran: Path) -> None:
    """Concatenate video clips."""
    daftar = BUILD / "concat.txt"
    daftar.write_text("\n".join(f"file '{c}'" for c in clips), encoding="utf-8")
    jalankan(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(daftar),
            "-c",
            "copy",
            str(keluaran),
        ]
    )


def main() -> int:
    BUILD.mkdir(parents=True, exist_ok=True)

    # Salin asset browser jika belum ada
    sumber_tryit = Path("/var/folders/b8/tsfnljj557542_6b_x9vry440000gn/T/cursor/screenshots/tryit.png")
    if sumber_tryit.exists() and not (BUILD / "04-tryit.png").exists():
        (BUILD / "04-tryit.png").write_bytes(sumber_tryit.read_bytes())

    for nama in ["01-hero.png", "02-ao-kanban.png", "03-demo.png"]:
        if not (BUILD / nama).exists():
            asal = ROOT / "docs" / "assets" / nama.replace("01-hero", "og-image").replace("02-ao-kanban", "ao-kanban").replace("03-demo", "demo-section")
            if nama == "01-hero.png":
                asal = BUILD / "01-hero.png"
            if asal.exists():
                pass  # already copied

    buat_slide_terminal()
    buat_slide_split()

    clips: list[Path] = []

    for seg in SEGmen:
        print(f"\n=== Segment {seg['id']} ===")
        if seg.get("gambar"):
            gambar = Path(seg["gambar"])
            if not gambar.exists():
                print(f"Missing image: {gambar}", file=sys.stderr)
                return 1
        else:
            gambar = buat_slide_teks(seg)

        audio, durasi = buat_narasi(seg)
        clip = BUILD / f"{seg['id']}.mp4"
        buat_clip_video(gambar, audio, durasi, clip)
        clips.append(clip)

    gabung_clips(clips, OUTPUT)

    probe = jalankan(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(OUTPUT),
        ]
    )
    durasi_total = float(probe.stdout.strip())
    print(f"\n✓ Video saved: {OUTPUT}")
    print(f"  Duration: {durasi_total:.1f}s ({durasi_total/60:.1f} min)")
    print("\nNext: upload to YouTube/Loom, then fill [VIDEO_URL] in docs/TIER-D-READY.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
