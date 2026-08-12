"""CLI entry point GreenLie."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from greenlie import __version__
from greenlie.analyze import analisis_repo
from greenlie.exceptions import GreenLieError

ROOT_PROYEK = Path(__file__).resolve().parents[2]
SAMPLE_SEBELUM = ROOT_PROYEK / "samples" / "before-agent-fix"
SAMPLE_SESUDAH = ROOT_PROYEK / "samples" / "after-agent-fix"


@click.group()
@click.version_option(version=__version__, prog_name="greenlie")
def main() -> None:
    """GreenLie - deteksi test backslide dari agent CI fix."""


@main.command("analyze")
@click.option(
    "--before",
    "jalur_sebelum",
    type=click.Path(exists=True, path_type=Path),
    help="Direktori test sebelum agent fix",
)
@click.option(
    "--after",
    "jalur_sesudah",
    type=click.Path(exists=True, path_type=Path),
    help="Direktori test sesudah agent fix",
)
@click.option("--format", "format_keluaran", type=click.Choice(["json", "table"]), default="table")
def perintah_analyze(
    jalur_sebelum: Path | None,
    jalur_sesudah: Path | None,
    format_keluaran: str,
) -> None:
    """Analisis integritas test antara versi before/after."""
    try:
        jalur_sebelum = jalur_sebelum or SAMPLE_SEBELUM
        jalur_sesudah = jalur_sesudah or SAMPLE_SESUDAH

        laporan = analisis_repo(jalur_sebelum, jalur_sesudah)
        _tampilkan_laporan(laporan, format_keluaran)

        # Exit 1 jika ada temuan backslide
        sys.exit(0 if not laporan.temuan else 1)

    except GreenLieError as err:
        click.echo(f"Error: {err}", err=True)
        sys.exit(2)
    except (FileNotFoundError, NotADirectoryError) as err:
        click.echo(f"Error: {err}", err=True)
        sys.exit(2)


def _tampilkan_laporan(laporan, format_keluaran: str) -> None:
    """Render laporan ke stdout."""
    if format_keluaran == "json":
        data = {
            "integrity_score": laporan.integrity_score,
            "assertion_dicek": laporan.assertion_dicek,
            "assertion_aman": laporan.assertion_aman,
            "metode": laporan.metode,
            "berkas_test": laporan.berkas_test,
            "temuan": [
                {
                    "id": t.id,
                    "severity": t.severity,
                    "sebelum": t.sebelum,
                    "sesudah": t.sesudah,
                    "alasan": t.alasan,
                    "berkas": t.berkas,
                    "baris": t.baris,
                    "confidence": t.confidence,
                }
                for t in laporan.temuan
            ],
        }
        click.echo(json.dumps(data, indent=2, ensure_ascii=False))
        return

    click.echo("")
    click.echo("=" * 60)
    click.echo(f"  GreenLie Report - Integrity: {laporan.integrity_score}%")
    click.echo("=" * 60)
    click.echo(
        f"  Assertions: {laporan.assertion_aman}/{laporan.assertion_dicek} intact"
    )
    click.echo(f"  Findings: {len(laporan.temuan)}")
    click.echo("")

    if not laporan.temuan:
        click.echo("  OK No test backslide detected")
        click.echo("")
        return

    for temuan in laporan.temuan:
        label = temuan.severity.upper()
        warna = {"CRITICAL": "red", "WARNING": "yellow"}.get(label, "white")
        click.echo(f"  [{click.style(label, fg=warna, bold=True)}] {temuan.id}")
        click.echo(f"    Before: {temuan.sebelum}")
        click.echo(f"    After:  {temuan.sesudah}")
        click.echo(f"    Reason: {temuan.alasan}")
        click.echo(f"    File:   {temuan.berkas}:{temuan.baris}")
        click.echo(f"    Confidence: {temuan.confidence:.0%}")
        click.echo("")

    click.echo("=" * 60)
    click.echo("")


if __name__ == "__main__":
    main()
