"""Package smoke tests for flight-trajectory."""

from flight_trajectory import __version__


def test_version_is_string() -> None:
    """Ensure the scaffold exposes a version string."""
    assert isinstance(__version__, str)
    assert __version__
