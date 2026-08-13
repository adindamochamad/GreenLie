#!/usr/bin/env python3
"""Generate GreenLie demo video — AO Kanban asli, browser, terminal, neural TTS."""

from __future__ import annotations

import asyncio
import shutil
import subprocess
import sys
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "docs" / "video-build"
OUTPUT = ROOT / "docs" / "GreenLie-demo.mp4"
FPS = 30
LEBAR = 1920
TINGGI = 1080
VOICE = "en-US-AndrewMultilingualNeural"
VOICE_RATE = "+2%"

# Screenshot AO Kanban asli dari user (prioritas path ini)
AO_SCREENSHOTS = [
    Path("/Users/mac/.cursor/projects/Users-mac-Development-GreenLie/assets/Screenshot_2026-08-12_at_20.21.44-15d30783-3f33-406a-9abe-47265496f3e1.png"),
    ROOT / "docs" / "video-build" / "02-ao-kanban.png",
    ROOT / "web" / "public" / "ao-kanban.png",
]

BG = (13, 15, 12)
HIJAU = (61, 255, 122)
MERAH = (255, 59, 48)
TEKS = (232, 228, 220)
ABU = (138, 143, 130)
ORanye = (196, 77, 46)

SEGmen = [
    {
        "id": "01-hook",
        "tipe": "animasi",
        "animasi": "hook",
        "durasi_min": 11.0,
        "narasi": "CI passed. Auth was broken. The agent didn't fix the bug — it fixed the test.",
    },
    {
        "id": "02-ao",
        "tipe": "ao_kanban",
        "durasi_min": 38.0,
        "narasi": (
            "GreenLie was built with Agent Orchestrator as the workspace. "
            "Parallel agents shipped the Python engine, the API, the demo site, "
            "and the sample fixtures — all visible on this board."
        ),
    },
    {
        "id": "03-hero",
        "tipe": "webm",
        "sumber": BUILD / "03-hero-rec.webm",
        "durasi_min": 13.0,
        "narasi": "Your Kanban says merge. Your tests say pass. Same agent fix — but two very different outcomes.",
    },
    {
        "id": "04-naive",
        "tipe": "webm",
        "sumber": BUILD / "04-demo-rec.webm",
        "durasi_min": 9.0,
        "narasi": "Naive merge: CI passes, board goes green, and nobody diffed the test file.",
    },
    {
        "id": "05-block",
        "tipe": "webm",
        "sumber": BUILD / "04-demo-rec.webm",
        "durasi_min": 13.0,
        "narasi": (
            "GreenLie blocks the merge. Integrity score: twenty-nine percent. "
            "Five critical findings — the test was weakened, not the bug."
        ),
        "offset_mulai": 4.0,
    },
    {
        "id": "06-tryit",
        "tipe": "webm",
        "sumber": BUILD / "05-tryit-rec.webm",
        "durasi_min": 15.0,
        "narasi": (
            "Run a live scan on the sample agent fix. "
            "Same backslide scenario — hit the API, get the verdict in milliseconds."
        ),
    },
    {
        "id": "07-terminal",
        "tipe": "webm",
        "sumber": BUILD / "06-terminal.webm",
        "durasi_min": 21.0,
        "narasi": (
            "Command line confirms it. GL-001: expect status toBe four-oh-one became toBeGreaterThan zero. "
            "Status five-hundred also passes. That's the green lie."
        ),
    },
    {
        "id": "08-end",
        "tipe": "animasi",
        "animasi": "end",
        "durasi_min": 14.0,
        "narasi": (
            "Try it at web-flax-xi-ten dot vercel dot app. "
            "Open source on GitHub. Built for The Orchestra hackathon with Agent Orchestrator. "
            "GreenLie — CI passed. Tests lied."
        ),
    },
]


def jalankan(perintah: list[str]) -> subprocess.CompletedResult:
    print("→", " ".join(perintah[:10]), "..." if len(perintah) > 10 else "")
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
    return 1 - pow(1 - t, 3)


def buat_frame_hook(frame: int, total: int) -> Image.Image:
    img = Image.new("RGB", (LEBAR, TINGGI), BG)
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
        alpha = int(255 * ee)
        if alpha <= 0:
            continue
        fill = tuple(int(c * alpha / 255) for c in warna)
        draw.text((120, y0 + indeks * 72 + int((1 - ee) * 40)), teks, fill=fill, font=font)

    if progress > 0.5:
        badge_t = easing(min(1.0, (progress - 0.5) / 0.3))
        bx, by = 120, 180
        draw.rounded_rectangle(
            (bx, by, bx + 280, by + 36), radius=4,
            outline=tuple(int(c * badge_t) for c in HIJAU), width=1,
        )
        draw.text(
            (bx + 12, by + 6), "CI PASS  |  44/44 tests",
            fill=tuple(int(c * badge_t) for c in HIJAU), font=cari_font(18, mono=True),
        )
    return img


def buat_frame_end(frame: int, total: int) -> Image.Image:
    img = Image.new("RGB", (LEBAR, TINGGI), BG)
    draw = ImageDraw.Draw(img)
    progress = easing(min(1.0, frame / (total * 0.8)))

    draw.text(
        (LEBAR // 2, 260), "GreenLie",
        fill=tuple(int(c * progress) for c in ORanye), font=cari_font(96), anchor="mm",
    )
    if progress > 0.25:
        t2 = easing(min(1.0, (progress - 0.25) / 0.55))
        for i, (teks, warna, ukuran) in enumerate([
            ("web-flax-xi-10.vercel.app", TEKS, 34),
            ("github.com/adindamochamad/GreenLie", ABU, 28),
            ("#agentorchestrator  ·  Built with Agent Orchestrator", HIJAU, 24),
        ]):
            draw.text(
                (LEBAR // 2, 400 + i * 56), teks,
                fill=tuple(int(c * t2) for c in warna),
                font=cari_font(ukuran, mono=(i < 2)), anchor="mm",
            )
    if progress > 0.65:
        t3 = easing(min(1.0, (progress - 0.65) / 0.35))
        draw.text(
            (LEBAR // 2, 620), "CI passed. Tests lied.",
            fill=tuple(int(c * t3) for c in MERAH), font=cari_font(42), anchor="mm",
        )
    return img


def animasi_ke_video(segmen: dict, keluaran: Path, durasi: float) -> None:
    total_frame = int(durasi * FPS)
    folder = BUILD / f"{segmen['id']}-frames"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)

    pembuat = buat_frame_hook if segmen["animasi"] == "hook" else buat_frame_end
    for f in range(total_frame):
        pembuat(f, total_frame).save(folder / f"frame_{f:04d}.png")

    jalankan([
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", str(folder / "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "20",
        str(keluaran),
    ])


def cari_screenshot_ao() -> Path:
    for jalur in AO_SCREENSHOTS:
        if jalur.exists():
            return jalur
    raise FileNotFoundError("Screenshot AO Kanban tidak ditemukan")


def buat_video_ao_kanban(jalur_gambar: Path, keluaran: Path, durasi: float) -> None:
    """Ken Burns pan pada screenshot AO asli — simulasi scroll Kanban."""
    img = Image.open(jalur_gambar).convert("RGB")
    lebar_asli, tinggi_asli = img.size

    # Crop area fokus board (hilangkan sidebar macOS jika ada)
    crop_kiri = int(lebar_asli * 0.08)
    crop_kanan = lebar_asli
    crop_atas = int(tinggi_asli * 0.05)
    crop_bawah = int(tinggi_asli * 0.95)
    img = img.crop((crop_kiri, crop_atas, crop_kanan, crop_bawah))
    lebar_crop, tinggi_crop = img.size

    # Scale up agar pan smooth
    skala = max(LEBAR / lebar_crop, TINGGI / tinggi_crop) * 1.35
    lebar_besar = int(lebar_crop * skala)
    tinggi_besar = int(tinggi_crop * skala)
    img_besar = img.resize((lebar_besar, tinggi_besar), Image.Resampling.LANCZOS)

    total_frame = int(durasi * FPS)
    folder = BUILD / "02-ao-kenburns-frames"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)

    # Pan horizontal: engine → needs you → wide shot
    x_mulai = 0
    x_akhir = max(0, lebar_besar - LEBAR)

    for f in range(total_frame):
        t = f / max(total_frame - 1, 1)
        # Ease in-out + hold di akhir
        if t < 0.75:
            tt = t / 0.75
            ee = tt * tt * (3 - 2 * tt)
        else:
            ee = 1.0
        x = int(x_mulai + (x_akhir - x_mulai) * ee)
        y = max(0, (tinggi_besar - TINGGI) // 2 - 20)

        frame = img_besar.crop((x, y, x + LEBAR, y + TINGGI))
        if frame.size != (LEBAR, TINGGI):
            frame = frame.resize((LEBAR, TINGGI), Image.Resampling.LANCZOS)
        frame.save(folder / f"frame_{f:04d}.jpg", quality=92)

    jalankan([
        "ffmpeg", "-y", "-framerate", str(FPS),
        "-i", str(folder / "frame_%04d.jpg"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "18",
        str(keluaran),
    ])


async def buat_narasi_async(teks: str, keluaran: Path) -> None:
    await edge_tts.Communicate(teks, VOICE, rate=VOICE_RATE).save(str(keluaran))


def buat_narasi(teks: str, keluaran: Path) -> float:
    mp3 = keluaran.with_suffix(".mp3")
    asyncio.run(buat_narasi_async(teks, mp3))
    m4a = keluaran.with_suffix(".m4a")
    jalankan(["ffmpeg", "-y", "-i", str(mp3), "-c:a", "aac", "-b:a", "192k", str(m4a)])
    return max(durasi_media(m4a), 0.1)


def normalisasi_webm(jalur: Path, keluaran: Path, durasi: float, offset: float = 0.0) -> None:
    vf = (
        f"scale={LEBAR}:{TINGGI}:force_original_aspect_ratio=decrease,"
        f"pad={LEBAR}:{TINGGI}:(ow-iw)/2:(oh-ih)/2:color=0x0D0F0C,"
        f"fps={FPS},"
        f"eq=contrast=1.06:brightness=0.02:saturation=1.1"
    )
    perintah = ["ffmpeg", "-y"]
    if offset > 0:
        perintah.extend(["-ss", f"{offset:.3f}"])
    perintah.extend([
        "-i", str(jalur), "-vf", vf, "-t", f"{durasi:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-an", str(keluaran),
    ])
    jalankan(perintah)


def gabung_video_audio(video: Path, audio: Path, keluaran: Path, durasi: float) -> None:
    jalankan([
        "ffmpeg", "-y", "-i", str(video), "-i", str(audio),
        "-t", f"{durasi:.3f}",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        str(keluaran),
    ])


def gabung_dengan_transisi(clips: list[Path], keluaran: Path) -> None:
    if len(clips) == 1:
        jalankan(["ffmpeg", "-y", "-i", str(clips[0]), "-c", "copy", str(keluaran)])
        return

    durasi_list = [durasi_media(c) for c in clips]
    fade = 0.4
    inputs: list[str] = []
    for c in clips:
        inputs.extend(["-i", str(c)])

    filter_parts: list[str] = []
    offset = durasi_list[0] - fade
    filter_parts.append(f"[0:v][1:v]xfade=transition=fade:duration={fade}:offset={offset:.3f}[v01]")
    filter_parts.append(f"[0:a][1:a]acrossfade=d={fade}[a01]")

    for i in range(2, len(clips)):
        v_prev = f"v{i-1:02d}" if i > 2 else "v01"
        a_prev = f"a{i-1:02d}" if i > 2 else "a01"
        offset += durasi_list[i - 1] - fade
        filter_parts.append(
            f"[{v_prev}][{i}:v]xfade=transition=fade:duration={fade}:offset={offset:.3f}[v{i:02d}]"
        )
        filter_parts.append(f"[{a_prev}][{i}:a]acrossfade=d={fade}[a{i:02d}]")

    v_final = f"v{len(clips)-1:02d}"
    a_final = f"a{len(clips)-1:02d}"
    fc = ";".join(filter_parts)

    jalankan([
        "ffmpeg", "-y", *inputs, "-filter_complex", fc,
        "-map", f"[{v_final}]", "-map", f"[{a_final}]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "17",
        "-c:a", "aac", "-b:a", "192k", str(keluaran),
    ])


def rekam_aset() -> None:
    print("\n=== Rekam browser (Playwright) ===")
    jalankan(["python3", str(ROOT / "scripts" / "video" / "rekam_browser.py")])

    print("\n=== Rekam terminal (VHS) ===")
    jalankan(["vhs", str(ROOT / "scripts" / "video" / "terminal.tape")])


def main() -> int:
    BUILD.mkdir(parents=True, exist_ok=True)
    rekam_aset()

    # Simpan copy screenshot AO asli
    ao_src = cari_screenshot_ao()
    ao_dst = BUILD / "02-ao-kanban-real.png"
    shutil.copy2(ao_src, ao_dst)
    print(f"✓ AO Kanban asli: {ao_src.name}")

    clips_final: list[Path] = []

    for seg in SEGmen:
        print(f"\n=== {seg['id']} ===")
        audio = BUILD / f"{seg['id']}-voice.m4a"
        durasi_narasi = buat_narasi(seg["narasi"], audio)
        # Scene 02: tambah 4 detik silence di akhir (Kanban breathe)
        tail_silent = 4.0 if seg["id"] == "02-ao" else 0.0
        durasi = max(durasi_narasi + tail_silent, seg["durasi_min"])

        video_raw = BUILD / f"{seg['id']}-raw.mp4"

        if seg["tipe"] == "animasi":
            animasi_ke_video(seg, video_raw, durasi)
        elif seg["tipe"] == "ao_kanban":
            buat_video_ao_kanban(ao_dst, video_raw, durasi)
        elif seg["tipe"] == "webm":
            sumber = seg["sumber"]
            if not sumber.exists():
                print(f"Missing: {sumber}", file=sys.stderr)
                return 1
            normalisasi_webm(sumber, video_raw, durasi, seg.get("offset_mulai", 0.0))
        else:
            print(f"Tipe tidak dikenal: {seg['tipe']}", file=sys.stderr)
            return 1

        clip = BUILD / f"{seg['id']}-final.mp4"
        if tail_silent > 0:
            # Pad audio dengan silence di akhir
            audio_padded = BUILD / f"{seg['id']}-voice-padded.m4a"
            jalankan([
                "ffmpeg", "-y", "-i", str(audio),
                "-af", f"apad=pad_dur={tail_silent}",
                "-t", f"{durasi:.3f}", "-c:a", "aac", "-b:a", "192k",
                str(audio_padded),
            ])
            gabung_video_audio(video_raw, audio_padded, clip, durasi)
        else:
            gabung_video_audio(video_raw, audio, clip, durasi)

        clips_final.append(clip)
        print(f"  → {durasi:.1f}s")

    temp = BUILD / "GreenLie-demo-composed.mp4"
    gabung_dengan_transisi(clips_final, temp)

    durasi_temp = durasi_media(temp)
    jalankan([
        "ffmpeg", "-y", "-i", str(temp),
        "-vf", f"fade=t=in:st=0:d=0.6,fade=t=out:st={max(0, durasi_temp - 0.8):.2f}:d=0.8",
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-preset", "medium", "-crf", "17",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        str(OUTPUT),
    ])

    total = durasi_media(OUTPUT)
    ao_durasi = durasi_media(BUILD / "02-ao-final.mp4")
    print(f"\n✓ Video: {OUTPUT}")
    print(f"  Durasi total: {total:.1f}s")
    print(f"  Scene AO Kanban: {ao_durasi:.1f}s (screenshot asli + Ken Burns pan)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
