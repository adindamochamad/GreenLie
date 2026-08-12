"""Entry point FastAPI GreenLie."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import ASAL_CORS_DIIZINKAN, SAMPLE_TERDAFTAR
from app.layanan import jalankan_analisis
from app.schemas import HealthResponse, LaporanAnalisisResponse, PermintaanAnalisis
from greenlie import __version__

aplikasi = FastAPI(
    title="GreenLie API",
    description="Detektor test backslide saat agent memperbaiki CI",
    version=__version__,
)

aplikasi.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@aplikasi.get("/health", response_model=HealthResponse)
def cek_kesehatan() -> HealthResponse:
    return HealthResponse(status="ok", version=__version__)


@aplikasi.post("/analyze", response_model=LaporanAnalisisResponse)
def analisis_sample(permintaan: PermintaanAnalisis) -> LaporanAnalisisResponse:
    konfigurasi = SAMPLE_TERDAFTAR.get(permintaan.sample)
    if konfigurasi is None:
        raise HTTPException(status_code=400, detail=f"Sample tidak dikenal: {permintaan.sample}")

    jalur_sebelum = konfigurasi["before"]
    jalur_sesudah = konfigurasi["after"]

    if not jalur_sebelum.is_dir() or not jalur_sesudah.is_dir():
        raise HTTPException(status_code=500, detail="Sample directory tidak ditemukan")

    return jalankan_analisis(jalur_sebelum, jalur_sesudah)


app = aplikasi
