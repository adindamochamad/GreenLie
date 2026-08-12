"""Ekstraksi assertion dari berkas test JS/TS dan Python."""

from __future__ import annotations

import re
from pathlib import Path

from greenlie.models import Assertion

# Pola matcher Jest/Vitest - urutan dari paling ketat ke paling longgar
POLA_JEST: list[tuple[str, int, str]] = [
    (r"expect\s*\([^)]+\)\s*\.toStrictEqual\s*\(", 95, "strict_equal"),
    (r"expect\s*\([^)]+\)\s*\.toEqual\s*\(", 85, "equal"),
    (r"expect\s*\([^)]+\)\s*\.toBe\s*\(\s*['\"][^'\"]+['\"]\s*\)", 90, "exact_string"),
    (r"expect\s*\([^)]+\)\s*\.toBe\s*\(\s*\d+\s*\)", 90, "exact_number"),
    (r"expect\s*\([^)]+\)\s*\.toBe\s*\(\s*true\s*\)", 88, "exact_bool"),
    (r"expect\s*\([^)]+\)\s*\.toBe\s*\(\s*false\s*\)", 88, "exact_bool"),
    (r"expect\s*\([^)]+\)\s*\.toMatch\s*\(\s*/[^/]+/\s*\)", 82, "regex_specific"),
    (r"expect\s*\([^)]+\)\s*\.toHaveLength\s*\(\s*\d+\s*\)", 80, "length_exact"),
    (r"expect\s*\([^)]+\)\s*\.toThrow\s*\(", 85, "throws"),
    (r"expect\s*\([^)]+\)\s*\.toBeGreaterThanOrEqual\s*\(\s*\d+\s*\)", 55, "range_gte"),
    (r"expect\s*\([^)]+\)\s*\.toBeGreaterThan\s*\(\s*\d+\s*\)", 50, "range_gt"),
    (r"expect\s*\([^)]+\)\s*\.toBeLessThan\s*\(\s*\d+\s*\)", 50, "range_lt"),
    (r"expect\s*\([^)]+\)\s*\.toBeTruthy\s*\(\s*\)", 35, "truthy"),
    (r"expect\s*\([^)]+\)\s*\.toBeDefined\s*\(\s*\)", 30, "defined"),
    (r"expect\s*\([^)]+\)\s*\.not\s*\.toBeNull\s*\(\s*\)", 75, "not_null"),
]

# Pola pytest
POLA_PYTEST: list[tuple[str, int, str]] = [
    (r"assert\s+[^#\n]+==\s*['\"][^'\"]+['\"]", 90, "assert_exact_string"),
    (r"assert\s+[^#\n]+==\s*\d+", 90, "assert_exact_number"),
    (r"assert\s+[^#\n]+\s+is\s+not\s+None", 75, "assert_not_none"),
    (r"assert\s+[^#\n]+\s+is\s+True", 88, "assert_bool"),
    (r"assert\s+[^#\n]+\s+is\s+False", 88, "assert_bool"),
    (r"pytest\.raises\s*\(", 85, "raises"),
    (r"assert\s+[^#\n]+", 60, "assert_loose"),
]


def apakah_berkas_test(jalur: Path) -> bool:
    """Cek apakah berkas termasuk file test."""
    nama = jalur.name.lower()
    if nama.startswith("test_") and nama.endswith(".py"):
        return True
    if ".test." in nama or ".spec." in nama:
        return True
    if nama.endswith("_test.py"):
        return True
    return jalur.parent.name in {"tests", "__tests__", "test"}


def ekstrak_assertion(isi: str, jalur_berkas: Path) -> list[Assertion]:
    """Ekstrak semua assertion dari isi berkas test."""
    if jalur_berkas.suffix == ".py":
        pola_list = POLA_PYTEST
    else:
        pola_list = POLA_JEST

    baris_list = isi.splitlines()
    hasil: list[Assertion] = []

    for nomor_baris, baris in enumerate(baris_list, start=1):
        baris_bersih = baris.strip()
        if not baris_bersih or baris_bersih.startswith("//") or baris_bersih.startswith("#"):
            continue

        for pola, ketat, jenis in pola_list:
            if re.search(pola, baris_bersih):
                hasil.append(
                    Assertion(
                        teks=baris_bersih,
                        baris=nomor_baris,
                        tingkat_ketat=ketat,
                        jenis=jenis,
                    )
                )
                break

    return hasil


def baca_berkas_test(jalur: Path) -> str:
    """Baca isi berkas test."""
    return jalur.read_text(encoding="utf-8")
