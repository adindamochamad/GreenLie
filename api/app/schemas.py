"""Skema request/response API GreenLie."""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    version: str


class PermintaanAnalisis(BaseModel):
    sample: str = Field(default="naive-agent", description="Sample bawaan untuk demo")


class TemuanResponse(BaseModel):
    id: str
    severity: str
    sebelum: str
    sesudah: str
    alasan: str
    berkas: str
    baris: int
    confidence: float


class LaporanAnalisisResponse(BaseModel):
    integrity_score: int
    assertion_dicek: int
    assertion_aman: int
    metode: str
    duration_ms: int
    berkas_test: list[str]
    temuan: list[TemuanResponse]
