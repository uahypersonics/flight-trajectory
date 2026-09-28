# flight-trajectory

Trajectory utilities for atmospheric and flight mechanics workflows.

[![Test](https://github.com/uahypersonics/flight-trajectory/actions/workflows/test.yml/badge.svg)](https://github.com/uahypersonics/flight-trajectory/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/flight-trajectory)](https://pypi.org/project/flight-trajectory/)
[![Docs](https://img.shields.io/badge/docs-zensical-blue)](https://uahypersonics.github.io/flight-trajectory/)
[![License](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.11-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Install

```bash
pip install flight-trajectory
```

## Quick Start

### CLI

```bash
flight-trajectory --help
```

### Python API

```python
import flight_trajectory

print(flight_trajectory.__version__)
```

## Development

```bash
pip install -e ".[dev]"
pytest tests/ -q
ruff check src/ tests/
```

## Documentation

Project documentation is built with Zensical and published at:

https://uahypersonics.github.io/flight-trajectory/

## Versioning & Releasing

This project uses [Semantic Versioning](https://semver.org/) (`vMAJOR.MINOR.PATCH`).

To publish a new version to PyPI:

1. Commit and push to `main`
2. Tag and push:
	```bash
	git tag -a vMAJOR.MINOR.PATCH -m "Release vMAJOR.MINOR.PATCH"
	git push origin vMAJOR.MINOR.PATCH
	```

The GitHub Actions workflow will build and publish to PyPI via Trusted Publishing.

## License

GNU General Public License v3.0 or later. See [LICENSE](LICENSE) for the
complete license terms.