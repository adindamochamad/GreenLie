"""Orkestrasi analisis GreenLie."""

from __future__ import annotations

from pathlib import Path

from greenlie.detector import analisis_direktori
from greenlie.models import LaporanIntegritas


def analisis_repo(
    jalur_sebelum: str | Path,
    jalur_sesudah: str | Path,
) -> LaporanIntegritas:
    """Jalankan analisis lengkap: before agent fix vs after agent fix."""
    return analisis_direktori(Path(jalur_sebelum), Path(jalur_sesudah))
