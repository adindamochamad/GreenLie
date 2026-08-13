"""Ekstraksi assertion dari berkas test JS/TS dan Python."""

from __future__ import annotations

import re
from pathlib import Path

from greenlie.models import Assertion

# Pola matcher Jest/Vitest - urutan dari paling ketat ke paling longgar.
# Urutan penting: first match wins per baris.
POLA_JEST: list[tuple[str, int, str]] = [
    # Strict structural comparisons
    (r"expect\s*\(.+?\)\s*\.toStrictEqual\s*\(", 95, "strict_equal"),
    (r"expect\s*\(.+?\)\s*\.toEqual\s*\(", 85, "equal"),
    (r"expect\s*\(.+?\)\s*\.toMatchObject\s*\(", 82, "match_object"),
    # Exact literals
    (r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*['\"][^'\"]+['\"]\s*\)", 90, "exact_string"),
    (r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*\d+(?:\.\d+)?\s*\)", 90, "exact_number"),
    (r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*true\s*\)", 88, "exact_bool"),
    (r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*false\s*\)", 88, "exact_bool"),
    (r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*null\s*\)", 88, "exact_null"),
    # Exact identifier / dotted constant (e.g. HttpStatus.UNAUTHORIZED, ROLES.ADMIN)
    # Slightly below literal to acknowledge indirection but still treated as exact.
    (
        r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)+\s*\)",
        82,
        "exact_dotted",
    ),
    (
        r"expect\s*\(.+?\)\s*\.toBe\s*\(\s*[A-Za-z_$][\w$]*\s*\)",
        80,
        "exact_identifier",
    ),
    # Specific matchers
    (r"expect\s*\(.+?\)\s*\.toMatch\s*\(\s*/[^/]+/\s*\)", 82, "regex_specific"),
    (r"expect\s*\(.+?\)\s*\.toHaveLength\s*\(\s*\d+\s*\)", 80, "length_exact"),
    (r"expect\s*\(.+?\)\s*\.toContain\s*\(\s*['\"][^'\"]+['\"]\s*\)", 78, "contain_string"),
    (r"expect\s*\(.+?\)\s*\.toContain\s*\(\s*\d+\s*\)", 78, "contain_number"),
    # Exception matchers - toThrow with arg vs empty
    (
        r"expect\s*\(.+?\)\s*\.toThrow\s*\(\s*['\"][^'\"]+['\"]\s*\)",
        88,
        "throws_message",
    ),
    (
        r"expect\s*\(.+?\)\s*\.toThrow\s*\(\s*[A-Za-z_$][\w$.]*\s*\)",
        85,
        "throws_specific",
    ),
    (r"expect\s*\(.+?\)\s*\.toThrow\s*\(\s*\)", 55, "throws_generic"),
    (r"expect\s*\(.+?\)\s*\.toThrow\b", 55, "throws_bare"),
    # Negated matchers (weaker than positive exact, but still assertive)
    (
        r"expect\s*\(.+?\)\s*\.not\s*\.toBe\s*\(\s*(?:['\"][^'\"]*['\"]|\d+|true|false|null|[A-Za-z_$][\w$.]*)\s*\)",
        70,
        "not_exact",
    ),
    (r"expect\s*\(.+?\)\s*\.not\s*\.toEqual\s*\(", 70, "not_equal"),
    (r"expect\s*\(.+?\)\s*\.not\s*\.toBeNull\s*\(\s*\)", 75, "not_null"),
    (r"expect\s*\(.+?\)\s*\.not\s*\.toBeUndefined\s*\(\s*\)", 60, "not_undefined"),
    # Loose numeric ranges
    (r"expect\s*\(.+?\)\s*\.toBeGreaterThanOrEqual\s*\(\s*\d+\s*\)", 55, "range_gte"),
    (r"expect\s*\(.+?\)\s*\.toBeLessThanOrEqual\s*\(\s*\d+\s*\)", 55, "range_lte"),
    (r"expect\s*\(.+?\)\s*\.toBeGreaterThan\s*\(\s*\d+\s*\)", 50, "range_gt"),
    (r"expect\s*\(.+?\)\s*\.toBeLessThan\s*\(\s*\d+\s*\)", 50, "range_lt"),
    # Loosest matchers
    (r"expect\s*\(.+?\)\s*\.toBeTruthy\s*\(\s*\)", 35, "truthy"),
    (r"expect\s*\(.+?\)\s*\.toBeFalsy\s*\(\s*\)", 35, "falsy"),
    (r"expect\s*\(.+?\)\s*\.toBeDefined\s*\(\s*\)", 30, "defined"),
    (r"expect\s*\(.+?\)\s*\.toBeUndefined\s*\(\s*\)", 30, "undefined"),
    # Fallback: any generic toEqual(x) with identifier / expression
    (r"expect\s*\(.+?\)\s*\.toBe\s*\(", 60, "to_be_generic"),
]

# Pola pytest
POLA_PYTEST: list[tuple[str, int, str]] = [
    (r"assert\s+[^#\n]+==\s*['\"][^'\"]+['\"]", 90, "assert_exact_string"),
    (r"assert\s+[^#\n]+==\s*\d+(?:\.\d+)?", 90, "assert_exact_number"),
    (r"assert\s+[^#\n]+==\s*[A-Z][A-Za-z0-9_.]*", 82, "assert_exact_constant"),
    (r"assert\s+[^#\n]+\s+is\s+not\s+None", 75, "assert_not_none"),
    (r"assert\s+[^#\n]+\s+is\s+True", 88, "assert_bool_true"),
    (r"assert\s+[^#\n]+\s+is\s+False", 88, "assert_bool_false"),
    (r"pytest\.raises\s*\(\s*[A-Za-z_][\w.]*\s*\)", 85, "raises_specific"),
    (r"pytest\.raises\s*\(\s*\)", 55, "raises_generic"),
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
