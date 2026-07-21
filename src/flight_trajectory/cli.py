"""Command-line entry point for flight-trajectory."""

from __future__ import annotations

import typer

app = typer.Typer(
    help="Trajectory utilities for atmospheric and flight mechanics workflows."
)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Run the scaffolded CLI."""
    # check
    if ctx.invoked_subcommand is not None:
        return

    # write
    typer.echo("flight-trajectory: under construction")


@app.command()
def version() -> None:
    """Print the package version."""
    # read
    from flight_trajectory import __version__

    # write
    typer.echo(__version__)


if __name__ == "__main__":
    app()
