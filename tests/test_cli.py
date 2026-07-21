"""CLI smoke tests for flight-trajectory."""

from typer.testing import CliRunner

from flight_trajectory.cli import app

runner = CliRunner()


def test_cli_help() -> None:
    """Ensure the scaffolded CLI exposes help."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Trajectory utilities" in result.output


def test_cli_default_message() -> None:
    """Ensure the scaffolded CLI prints a placeholder message."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "under construction" in result.output
