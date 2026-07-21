"""Top-level package for flight-trajectory."""

from importlib.metadata import PackageNotFoundError, version

# read installed package metadata when available
try:
    __version__ = version("flight-trajectory")
except PackageNotFoundError:
    # default for source-tree execution where package metadata is absent
    __version__ = "0+unknown"

__all__ = ["__version__"]
