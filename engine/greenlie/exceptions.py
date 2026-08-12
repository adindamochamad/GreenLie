"""Pengecualian khusus engine GreenLie."""


class GreenLieError(Exception):
    """Error dasar GreenLie."""


class BerkasTidakValidError(GreenLieError):
    """Berkas diff atau test tidak bisa diproses."""
