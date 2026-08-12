#!/usr/bin/env python3
"""Bangun demo video GreenLie kualitas pro — browser nyata, VHS terminal, neural TTS."""

from __future__ import annotations

import asyncio
import math
import subprocess
import sys
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "docs" / "video-build"
OUTPUT = ROOT / "docs" / "GreenLie-demo.mp4"
FPS = 30
LEBAR = 1920
TINGGI = 1080
VOICE = "en-US-AndrewMultilingualNeural"
VOICE_RATE = "+4%"

BG = (13, 15, 12)
HIJAU = (61, 255, 122)
MERAH = (255, 59, 48)
TEKS = (232, 228, 220)
ABU = (138, 143, 130)
ORanye = (196, 77, 46)

SEGmen = [
    {
        "id": "01-hook",
        "video": None,
        "animasi": "hook",
        "durasi_min": 9.0,
        "narasi": "CI passed. Auth was broken. The agent didn't fix the bug — it fixed the test.",
    },
    {
        "id": "02-ao",
        "video": BUILD / "02-ao-rec.webm",
        "durasi_min": 8.0,
        "narasi": "GreenLie was built with Agent Orchestrator — parallel agents on engine, API, and demo site.",
    },
    {
        "id": "03-hero",
        "video": BUILD / "03-hero-rec.webm",
        "durasi_min": 7.5,
        "narasi": "Same agent fix. Two outcomes. Naive merge — board green, CI passes.",
    },
    {
        "id": "04-demo",
        "video": BUILD / "04-demo-rec.webm",
        "durasi_min": 10.0,
        "narasi": "GreenLie flags the backslide. Integrity twenty-nine percent. Five critical findings. Merge blocked.",
    },
    {
        "id": "05-tryit",
        "video": BUILD / "05-tryit-rec.webm",
        "durasi_min": 9.0,
        "narasi": "Live API scan on the sample agent fix — same engine, same verdict.",
    },
    {
        "id": "06-terminal",
        "video": BUILD / "06-terminal.webm",
        "durasi_min": 12.0,
        "narasi": "Command line: GL-001. toBe four oh one became toBeGreaterThan zero. Five hundred also passes.",
    },
    {
        "id": "08-end",
        "video": None,
        "animasi": "end",
        "durasi_min": 10.0,
        "narasi": "Try it at web-flax-xi-10.vercel.app. GreenLie — CI passed. Tests lied.",
    },
]


def jalankan(perintah: list[str]) -> subprocess.CompletedResult:
    print("→", " ".join(perintah[:8]), "..." if len(perintah) > 8 else "")
    return subprocess.run(perintah, check=True, capture_output=True, text=True)


def durasi_media(jalur: Path) -> float:
    hasil = jalankan(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(jalur),
        ]
    )
    return float(hasil.stdout.strip())


def cari_font(ukuran: int, mono: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    kandidat = (
        ["/System/Library/Fonts/Menlo.ttc", "/System/Library/Fonts/Supplemental/Andale Mono.ttf"]
        if mono
        else [
            "/System/Library/Fonts/Supplemental/Georgia.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Menlo.ttc",
        ]
    )
    for jalur in kandidat:
        if Path(jalur).exists():
            try:
                return ImageFont.truetype(jalur, ukuran)
            except OSError:
                continue
    return ImageFont.load_default()


def easing(t: float) -> float:
    """Ease-out cubic."""
    return 1 - pow(1 - t, 3)


def buat_frame_animasi_hook(frame: int, total: int) -> Image.Image:
    """Frame animasi hook dengan fade + slide."""
    img = Image.new("RGB", (LEBAR, TINGGI), BG)
    draw = ImageDraw.Draw(img)

    # Glow halus di atas
    overlay = Image.new("RGB", (LEBAR, TINGGI), BG)
    od = ImageDraw.Draw(overlay)
    for r in range(300, 0, -15):
        g = int(12 * (1 - r / 300))
        od.ellipse((LEBAR // 2 - r, 60, LEBAR // 2 + r, 60 + r), fill=(g, g + 8, g))
    img = Image.blend(img, overlay, 0.35)
    draw = ImageDraw.Draw(img)
    progress = min(1.0, frame / (total * 0.85))

    baris = [
        ("GreenLie", cari_font(108), HIJAU, 0),
        ("CI passed. Auth was broken.", cari_font(48), TEKS, 1),
        ("The agent didn't fix the bug —", cari_font(38), ABU, 2),
        ("it fixed the test.", cari_font(44), MERAH, 3),
    ]

    y0 = 300
    for teks, font, warna, indeks in baris:
        delay = indeks * 0.12
        t = max(0.0, min(1.0, (progress - delay) / 0.35))
        ee = easing(t)
        offset_y = int((1 - ee) * 40)
        alpha = int(255 * ee)
        if alpha <= 0:
            continue
        fill = tuple(int(c * alpha / 255) for c in warna)
        draw.text((120, y0 + indeks * 72 + offset_y), teks, fill=fill, font=font)

    # Badge CI pass
    if progress > 0.5:
        badge_t = easing(min(1.0, (progress - 0.5) / 0.3))
        bx, by = 120, 180
        draw.rounded_rectangle(
            (bx, by, bx + 280, by + 36),
            radius=4,
            outline=tuple(int(c * badge_t) for c in HIJAU),
            width=1,
        )
        draw.text((bx + 12, by + 6), "CI PASS  |  44/44 tests", fill=tuple(int(c * badge_t) for c in HIJAU), font=cari_font(18, mono=True))

    return img


def buat_frame_animasi_end(frame: int, total: int) -> Image.Image:
    """Frame animasi end card."""
    img = Image.new("RGB", (LEBAR, TINGGI), BG)
    draw = ImageDraw.Draw(img)
    progress = easing(min(1.0, frame / (total * 0.8)))

    draw.text((LEBAR // 2, 280), "GreenLie", fill=tuple(int(c * progress) for c in ORanye), font=cari_font(96), anchor="mm")

    if progress > 0.3:
        t2 = easing(min(1.0, (progress - 0.3) / 0.5))
        for i, (teks, warna, ukuran) in enumerate([
            ("web-flax-xi-10.vercel.app", TEKS, 34),
            ("github.com/adindamochamad/GreenLie", ABU, 28),
            ("#agentorchestrator  ·  Built with Agent Orchestrator", HIJAU, 24),
        ]):
            draw.text(
                (LEBAR // 2, 420 + i * 56),
                teks,
                fill=tuple(int(c * t2) for c in warna),
                font=cari_font(ukuran, mono=(i < 2)),
                anchor="mm",
            )

    if progress > 0.6:
        t3 = easing(min(1.0, (progress - 0.6) / 0.4))
        draw.text(
            (LEBAR // 2, 640),
            "CI passed. Tests lied.",
            fill=tuple(int(c * t3) for c in MERAH),
            font=cari_font(42),
            anchor="mm",
        )

    return img


def animasi_ke_video(segmen: dict, keluaran: Path) -> None:
    """Render animasi teks menjadi mp4."""
    total_frame = int(segmen["durasi_min"] * FPS)
    folder = BUILD / f"{segmen['id']}-frames"
    folder.mkdir(exist_ok=True)

    pembuat = buat_frame_animasi_hook if segmen["animasi"] == "hook" else buat_frame_animasi_end
    for f in range(total_frame):
        pembuat(f, total_frame).save(folder / f"frame_{f:04d}.png")

    jalankan(
        [
            "ffmpeg", "-y", "-framerate", str(FPS),
            "-i", str(folder / "frame_%04d.png"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-preset", "slow", "-crf", "18",
            str(keluaran),
        ]
    )


async def buat_narasi_async(teks: str, keluaran: Path) -> None:
    komunikasi = edge_tts.Communicate(teks, VOICE, rate=VOICE_RATE)
    await komunikasi.save(str(keluaran))


def buat_narasi(teks: str, keluaran: Path) -> float:
    mp3 = keluaran.with_suffix(".mp3")
    asyncio.run(buat_narasi_async(teks, mp3))
    m4a = keluaran.with_suffix(".m4a")
    jalankan(["ffmpeg", "-y", "-i", str(mp3), "-c:a", "aac", "-b:a", "192k", str(m4a)])
    return max(durasi_media(m4a), 0.1)


def normalisasi_video_masuk(jalur: Path, keluaran: Path, durasi_target: float) -> None:
    """Scale, pad, extend video ke 1080p dan match durasi narasi."""
    vf = (
        f"scale={LEBAR}:{TINGGI}:force_original_aspect_ratio=decrease,"
        f"pad={LEBAR}:{TINGGI}:(ow-iw)/2:(oh-ih)/2:color=0x0D0F0C,"
        f"fps={FPS},"
        f"tpad=stop_mode=clone:stop_duration={max(0, durasi_target - durasi_media(jalur)):.3f},"
        f"eq=contrast=1.05:brightness=0.02:saturation=1.08,"
        f"unsharp=5:5:0.4:5:5:0.0"
    )
    jalankan(
        [
            "ffmpeg", "-y", "-i", str(jalur),
            "-vf", vf, "-t", f"{durasi_target:.3f}",
            "-c:v", "libx264", "-preset", "slow", "-crf", "18",
            "-pix_fmt", "yuv420p", "-an",
            str(keluaran),
        ]
    )


def gabung_video_audio(video: Path, audio: Path, keluaran: Path, durasi: float) -> None:
    jalankan(
        [
            "ffmpeg", "-y",
            "-i", str(video), "-i", str(audio),
            "-t", f"{durasi:.3f}",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
            str(keluaran),
        ]
    )


def gabung_dengan_transisi(clips: list[Path], keluaran: Path) -> None:
    """Gabung clips dengan xfade fade antar segmen."""
    if len(clips) == 1:
        jalankan(["ffmpeg", "-y", "-i", str(clips[0]), "-c", "copy", str(keluaran)])
        return

    durasi_list = [durasi_media(c) for c in clips]
    fade = 0.35
    inputs = []
    for c in clips:
        inputs.extend(["-i", str(c)])

    filter_parts = []
    offset = durasi_list[0] - fade
    filter_parts.append(f"[0:v][1:v]xfade=transition=fade:duration={fade}:offset={offset:.3f}[v01]")
    filter_parts.append(f"[0:a][1:a]acrossfade=d={fade}[a01]")

    for i in range(2, len(clips)):
        v_prev = f"v{i-1:02d}" if i > 2 else "v01"
        a_prev = f"a{i-1:02d}" if i > 2 else "a01"
        v_out = f"v{i:02d}"
        a_out = f"a{i:02d}"
        offset += durasi_list[i - 1] - fade
        filter_parts.append(
            f"[{v_prev}][{i}:v]xfade=transition=fade:duration={fade}:offset={offset:.3f}[{v_out}]"
        )
        filter_parts.append(f"[{a_prev}][{i}:a]acrossfade=d={fade}[{a_out}]")

    v_final = f"v{len(clips)-1:02d}"
    a_final = f"a{len(clips)-1:02d}"
    fc = ";".join(filter_parts)

    jalankan(
        [
            "ffmpeg", "-y", *inputs,
            "-filter_complex", fc,
            "-map", f"[{v_final}]", "-map", f"[{a_final}]",
            "-c:v", "libx264", "-preset", "slow", "-crf", "17",
            "-c:a", "aac", "-b:a", "192k",
            str(keluaran),
        ]
    )


def rekam_aset() -> None:
    """Rekam browser + terminal jika belum ada."""
    print("\n=== Rekam aset ===")
    jalankan(["python3", str(ROOT / "scripts" / "video" / "rekam_browser.py")])
    jalankan(["vhs", str(ROOT / "scripts" / "video" / "terminal.tape")])


def main() -> int:
    BUILD.mkdir(parents=True, exist_ok=True)

    # Selalu rekam ulang agar fresh
    rekam_aset()

    clips_final: list[Path] = []

    for seg in SEGmen:
        print(f"\n=== Segment {seg['id']} ===")
        audio = BUILD / f"{seg['id']}-voice.m4a"
        durasi_narasi = buat_narasi(seg["narasi"], audio)
        durasi = max(durasi_narasi, seg["durasi_min"])

        video_raw = BUILD / f"{seg['id']}-raw.mp4"
        if seg.get("animasi"):
            animasi_ke_video({**seg, "durasi_min": durasi}, video_raw)
        else:
            sumber = seg["video"]
            if not sumber or not sumber.exists():
                print(f"Missing: {sumber}", file=sys.stderr)
                return 1
            normalisasi_video_masuk(sumber, video_raw, durasi)

        clip = BUILD / f"{seg['id']}-final.mp4"
        gabung_video_audio(video_raw, audio, clip, durasi)
        clips_final.append(clip)

    temp = BUILD / "GreenLie-demo-composed.mp4"
    gabung_dengan_transisi(clips_final, temp)

    durasi_temp = durasi_media(temp)
    jalankan(
        [
            "ffmpeg", "-y", "-i", str(temp),
            "-vf", f"fade=t=in:st=0:d=0.5,fade=t=out:st={max(0, durasi_temp - 0.6):.2f}:d=0.6",
            "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
            "-c:v", "libx264", "-preset", "slow", "-crf", "17",
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart",
            str(OUTPUT),
        ]
    )

    durasi_total = durasi_media(OUTPUT)
    print(f"\n✓ Pro video: {OUTPUT} ({durasi_total:.1f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
