"""Test detektor GreenLie - deteksi backslide, guard false positive, edge case."""

from pathlib import Path

import pytest

from greenlie.analyze import analisis_repo
from greenlie.detector import analisis_direktori
from greenlie.parser_test import ekstrak_assertion

ROOT = Path(__file__).resolve().parents[2]
SEBELUM = ROOT / "samples" / "before-agent-fix"
SESUDAH = ROOT / "samples" / "after-agent-fix"


# ---------- Golden sample ----------


def test_analisis_sample_menemukan_backslide():
    """Sample agent fix harus menghasilkan minimal 3 temuan."""
    laporan = analisis_repo(SEBELUM, SESUDAH)
    assert laporan.integrity_score < 70
    assert len(laporan.temuan) >= 3
    assert any("TEST_BACKSLIDE" in t.alasan for t in laporan.temuan)


def test_analisis_sample_berkas_test_terdeteksi():
    """Engine harus menemukan berkas test auth."""
    laporan = analisis_repo(SEBELUM, SESUDAH)
    assert "tests/auth.test.js" in laporan.berkas_test


def test_golden_sample_score_exact():
    """Golden report harus tetap konsisten 29% / 5 findings untuk demo."""
    laporan = analisis_repo(SEBELUM, SESUDAH)
    assert laporan.integrity_score == 29
    assert len(laporan.temuan) == 5
    assert laporan.assertion_dicek == 7
    assert laporan.assertion_aman == 2


# ---------- Guard false positive ----------


def test_identical_file_zero_findings(tmp_path: Path):
    """Membandingkan direktori yang isinya persis sama harus 100% integrity."""
    isi = """
describe('x', () => {
  it('y', () => {
    expect(a).toBe(1);
    expect(b).toBe('ok');
  });
});
"""
    for sub in ["before/tests", "after/tests"]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert laporan.integrity_score == 100
    assert laporan.temuan == []


def test_empty_directory(tmp_path: Path):
    """Direktori kosong tidak boleh crash dan harus 100%."""
    (tmp_path / "before").mkdir()
    (tmp_path / "after").mkdir()
    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert laporan.integrity_score == 100
    assert laporan.assertion_dicek == 0
    assert laporan.temuan == []


def test_constant_refactor_not_flagged(tmp_path: Path):
    """toBe(401) -> toBe(HttpStatus.UNAUTHORIZED) adalah refactor, bukan backslide."""
    before = "expect(response.status).toBe(401);"
    after = "expect(response.status).toBe(HttpStatus.UNAUTHORIZED);"
    for sub, isi in [("before/tests", before), ("after/tests", after)]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert laporan.temuan == []
    assert laporan.integrity_score == 100


def test_identifier_refactor_not_flagged(tmp_path: Path):
    """toBe('admin') -> toBe(ROLES.ADMIN) tidak boleh di-flag critical."""
    before = "expect(user.role).toBe('admin');"
    after = "expect(user.role).toBe(ROLES.ADMIN);"
    for sub, isi in [("before/tests", before), ("after/tests", after)]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    # selisih strictness 90 -> 82 = 8, di bawah threshold 15
    assert laporan.temuan == []


def test_improvement_not_flagged(tmp_path: Path):
    """toBeDefined() -> toBe(200) adalah peningkatan strictness, tidak boleh di-flag."""
    before = "expect(response.status).toBeDefined();"
    after = "expect(response.status).toBe(200);"
    for sub, isi in [("before/tests", before), ("after/tests", after)]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert laporan.temuan == []


# ---------- Pattern coverage ----------


def test_toThrow_specific_to_generic_flagged(tmp_path: Path):
    """toThrow(ValidationError) -> toThrow() harus di-flag sebagai backslide."""
    before = "expect(() => parse(bad)).toThrow(ValidationError);"
    after = "expect(() => parse(bad)).toThrow();"
    for sub, isi in [("before/tests", before), ("after/tests", after)]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert len(laporan.temuan) == 1
    assert "toThrow" in laporan.temuan[0].alasan


def test_toEqual_to_defined_flagged(tmp_path: Path):
    """toEqual({...}) -> toBeDefined() harus di-flag."""
    before = "expect(user).toEqual({id: 1, email: 'x@y.com'});"
    after = "expect(user).toBeDefined();"
    for sub, isi in [("before/tests", before), ("after/tests", after)]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert len(laporan.temuan) == 1
    assert laporan.temuan[0].severity == "critical"


def test_toContain_to_defined_flagged(tmp_path: Path):
    """toContain('admin') -> toBeDefined() harus di-flag."""
    before = "expect(errors).toContain('admin');"
    after = "expect(errors).toBeDefined();"
    for sub, isi in [("before/tests", before), ("after/tests", after)]:
        (tmp_path / sub).mkdir(parents=True)
        (tmp_path / sub / "x.test.js").write_text(isi)

    laporan = analisis_direktori(tmp_path / "before", tmp_path / "after")
    assert len(laporan.temuan) == 1


# ---------- Parser sanity ----------


@pytest.mark.parametrize(
    "line,expected_type,expected_min_strict",
    [
        ("expect(x).toBe(401);", "exact_number", 88),
        ("expect(x).toBe('ok');", "exact_string", 88),
        ("expect(x).toBe(HttpStatus.OK);", "exact_dotted", 80),
        ("expect(x).toBe(expected);", "exact_identifier", 78),
        ("expect(x).toBeGreaterThan(0);", "range_gt", 45),
        ("expect(x).toBeDefined();", "defined", 25),
        ("expect(x).toBeTruthy();", "truthy", 30),
        ("expect(fn).toThrow(ValidationError);", "throws_specific", 80),
        ("expect(fn).toThrow();", "throws_generic", 50),
    ],
)
def test_parser_pattern_types(line: str, expected_type: str, expected_min_strict: int):
    hasil = ekstrak_assertion(line, Path("x.test.js"))
    assert len(hasil) == 1
    assert hasil[0].jenis == expected_type
    assert hasil[0].tingkat_ketat >= expected_min_strict


def test_pytest_pattern_recognized():
    line = "assert user.role == 'admin'"
    hasil = ekstrak_assertion(line, Path("test_x.py"))
    assert len(hasil) == 1
    assert hasil[0].jenis == "assert_exact_string"
