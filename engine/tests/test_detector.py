"""Test detektor GreenLie."""

from pathlib import Path

from greenlie.analyze import analisis_repo

ROOT = Path(__file__).resolve().parents[2]
SEBELUM = ROOT / "samples" / "before-agent-fix"
SESUDAH = ROOT / "samples" / "after-agent-fix"


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
