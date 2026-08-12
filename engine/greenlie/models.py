"""Model data inti engine GreenLie."""

from dataclasses import dataclass, field


@dataclass
class Assertion:
    """Satu assertion test yang diekstrak dari berkas."""

    teks: str
    baris: int
    tingkat_ketat: int
    jenis: str


@dataclass
class TemuanBackslide:
    """Satu temuan assertion yang melemah setelah agent fix."""

    id: str
    severity: str
    sebelum: str
    sesudah: str
    alasan: str
    berkas: str
    baris: int
    confidence: float


@dataclass
class LaporanIntegritas:
    """Laporan lengkap analisis integritas test."""

    integrity_score: int
    temuan: list[TemuanBackslide]
    assertion_dicek: int
    assertion_aman: int
    metode: str = "backslide_v1"
    berkas_test: list[str] = field(default_factory=list)
