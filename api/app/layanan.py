"""Layanan analisis GreenLie."""

from __future__ import annotations

import time
from pathlib import Path

from greenlie.analyze import analisis_repo

from app.schemas import LaporanAnalisisResponse, TemuanResponse


def jalankan_analisis(jalur_sebelum: Path, jalur_sesudah: Path) -> LaporanAnalisisResponse:
    """Jalankan analisis dan bungkus ke response API."""
    mulai = time.perf_counter()
    laporan = analisis_repo(jalur_sebelum, jalur_sesudah)
    durasi_ms = int((time.perf_counter() - mulai) * 1000)

    return LaporanAnalisisResponse(
        integrity_score=laporan.integrity_score,
        assertion_dicek=laporan.assertion_dicek,
        assertion_aman=laporan.assertion_aman,
        metode=laporan.metode,
        duration_ms=durasi_ms,
        berkas_test=laporan.berkas_test,
        temuan=[
            TemuanResponse(
                id=t.id,
                severity=t.severity,
                sebelum=t.sebelum,
                sesudah=t.sesudah,
                alasan=t.alasan,
                berkas=t.berkas,
                baris=t.baris,
                confidence=t.confidence,
            )
            for t in laporan.temuan
        ],
    )
