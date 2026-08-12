"""Konfigurasi API GreenLie."""

from pathlib import Path

ROOT_PROYEK = Path(__file__).resolve().parents[2]

SAMPLE_TERDAFTAR: dict[str, dict[str, Path]] = {
    "naive-agent": {
        "before": ROOT_PROYEK / "samples" / "before-agent-fix",
        "after": ROOT_PROYEK / "samples" / "after-agent-fix",
    },
}

ASAL_CORS_DIIZINKAN = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://*.vercel.app",
]
