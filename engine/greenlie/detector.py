"""Deteksi assertion weakening antara versi sebelum dan sesudah agent fix."""

from __future__ import annotations

import difflib
from pathlib import Path

from greenlie.models import Assertion, LaporanIntegritas, TemuanBackslide
from greenlie.parser_test import apakah_berkas_test, baca_berkas_test, ekstrak_assertion

# Jenis assertion yang dianggap "exact" untuk klasifikasi backslide.
JENIS_EXACT = {
    "exact_number",
    "exact_string",
    "exact_bool",
    "exact_null",
    "exact_identifier",
    "exact_dotted",
    "strict_equal",
    "equal",
    "match_object",
    "regex_specific",
    "length_exact",
    "contain_string",
    "contain_number",
    "throws_specific",
    "throws_message",
    "assert_exact_string",
    "assert_exact_number",
    "assert_exact_constant",
    "assert_bool_true",
    "assert_bool_false",
    "raises_specific",
}

JENIS_LONGGAR = {
    "truthy",
    "falsy",
    "defined",
    "undefined",
    "not_undefined",
    "throws_generic",
    "throws_bare",
    "raises_generic",
    "assert_loose",
    "to_be_generic",
}

JENIS_RANGE_PREFIX = ("range_",)


def _cocokkan_assertion(
    sebelum: list[Assertion],
    sesudah: list[Assertion],
    berkas: str,
) -> list[TemuanBackslide]:
    """Bandingkan assertion sebelum/sesudah dan deteksi pelemahan."""
    temuan: list[TemuanBackslide] = []
    indeks_sesudah = list(range(len(sesudah)))
    counter = 0

    for asrt_sebelum in sebelum:
        pasangan: Assertion | None = None
        indeks_pasangan = -1

        # Cari pasangan terdekat berdasarkan baris atau teks serupa
        for idx in indeks_sesudah:
            kandidat = sesudah[idx]
            if _assertion_serupa(asrt_sebelum, kandidat):
                pasangan = kandidat
                indeks_pasangan = idx
                break

        if pasangan is None:
            counter += 1
            temuan.append(
                TemuanBackslide(
                    id=f"GL-{counter:03d}",
                    severity="critical",
                    sebelum=asrt_sebelum.teks,
                    sesudah="*(assertion dihapus)*",
                    alasan="ASSERTION_DROPPED - agent menghapus assertion yang sebelumnya ada",
                    berkas=berkas,
                    baris=asrt_sebelum.baris,
                    confidence=0.95,
                )
            )
            continue

        indeks_sesudah.remove(indeks_pasangan)

        if pasangan.tingkat_ketat < asrt_sebelum.tingkat_ketat - 15:
            counter += 1
            selisih = asrt_sebelum.tingkat_ketat - pasangan.tingkat_ketat
            temuan.append(
                TemuanBackslide(
                    id=f"GL-{counter:03d}",
                    severity="critical" if selisih >= 30 else "warning",
                    sebelum=asrt_sebelum.teks,
                    sesudah=pasangan.teks,
                    alasan=_alasan_pelemahan(asrt_sebelum, pasangan),
                    berkas=berkas,
                    baris=pasangan.baris,
                    confidence=min(0.98, 0.7 + selisih / 100),
                )
            )

    return temuan


def _assertion_serupa(a: Assertion, b: Assertion) -> bool:
    """Heuristik: apakah dua assertion menguji hal yang sama."""
    if abs(a.baris - b.baris) <= 3:
        return True

    # Bandingkan subjek expect(...) yang sama
    import re

    subjek_a = re.search(r"expect\s*\(([^)]+)\)", a.teks)
    subjek_b = re.search(r"expect\s*\(([^)]+)\)", b.teks)
    if subjek_a and subjek_b and subjek_a.group(1).strip() == subjek_b.group(1).strip():
        return True

    assert_a = re.search(r"assert\s+([^=!<>]+)", a.teks)
    assert_b = re.search(r"assert\s+([^=!<>]+)", b.teks)
    if assert_a and assert_b and assert_a.group(1).strip() == assert_b.group(1).strip():
        return True

    return difflib.SequenceMatcher(None, a.teks, b.teks).ratio() > 0.55


def _alasan_pelemahan(sebelum: Assertion, sesudah: Assertion) -> str:
    """Buat alasan human-readable untuk pelemahan assertion."""
    # Check specific patterns before the generic exact-to-loose branch.
    if sebelum.jenis in {"throws_specific", "throws_message"} and sesudah.jenis in {
        "throws_generic",
        "throws_bare",
    }:
        return "TEST_BACKSLIDE - expect().toThrow(SpecificError) diganti toThrow() generic"

    if any(sesudah.jenis.startswith(p) for p in JENIS_RANGE_PREFIX) and sebelum.jenis in {
        "exact_number",
        "exact_identifier",
        "exact_dotted",
    }:
        return "TEST_BACKSLIDE - status code exact diganti range yang menerima semua response"

    if sebelum.jenis == "regex_specific" and sesudah.jenis in JENIS_LONGGAR:
        return "TEST_BACKSLIDE - pengecekan string regex diganti truthy/defined"

    if sebelum.jenis in {"strict_equal", "equal", "match_object"} and sesudah.jenis in JENIS_LONGGAR:
        return "TEST_BACKSLIDE - deep equality diganti truthy/defined"

    if sebelum.jenis in {"contain_string", "contain_number"} and sesudah.jenis in JENIS_LONGGAR:
        return "TEST_BACKSLIDE - toContain(spesifik) diganti truthy/defined"

    if sesudah.jenis in JENIS_LONGGAR and sebelum.jenis in JENIS_EXACT:
        return "TEST_BACKSLIDE - assertion exact diganti truthy/defined yang selalu pass"

    return f"TEST_BACKSLIDE - ketat {sebelum.tingkat_ketat} -> {sesudah.tingkat_ketat}"


def _hitung_skor_integritas(dicek: int, aman: int) -> int:
    """Skor 0-100 - persentase assertion yang tidak melemah."""
    if dicek == 0:
        return 100
    return max(0, min(100, round(100 * aman / dicek)))


def analisis_direktori(
    jalur_sebelum: Path,
    jalur_sesudah: Path,
) -> LaporanIntegritas:
    """Bandingkan dua direktori test (before vs after agent fix)."""
    temuan_gabungan: list[TemuanBackslide] = []
    berkas_test: list[str] = []
    total_dicek = 0
    total_aman = 0

    # Kumpulkan berkas test dari direktori sebelum
    berkas_sebelum = {
        f.relative_to(jalur_sebelum).as_posix(): f
        for f in jalur_sebelum.rglob("*")
        if f.is_file() and apakah_berkas_test(f)
    }

    for rel, path_sebelum in berkas_sebelum.items():
        path_sesudah = jalur_sesudah / rel
        if not path_sesudah.is_file():
            continue

        isi_sebelum = baca_berkas_test(path_sebelum)
        isi_sesudah = baca_berkas_test(path_sesudah)

        asrt_sebelum = ekstrak_assertion(isi_sebelum, path_sebelum)
        asrt_sesudah = ekstrak_assertion(isi_sesudah, path_sesudah)

        total_dicek += len(asrt_sebelum)
        temuan_berkas = _cocokkan_assertion(asrt_sebelum, asrt_sesudah, rel)
        temuan_gabungan.extend(temuan_berkas)
        total_aman += len(asrt_sebelum) - len(temuan_berkas)
        berkas_test.append(rel)

    return LaporanIntegritas(
        integrity_score=_hitung_skor_integritas(total_dicek, total_aman),
        temuan=temuan_gabungan,
        assertion_dicek=total_dicek,
        assertion_aman=total_aman,
        berkas_test=berkas_test,
    )
