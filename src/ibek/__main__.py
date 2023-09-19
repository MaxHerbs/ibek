from typing import Optional

import typer
from ruamel.yaml import YAML

from ibek.ioc_cmds.commands import ioc_cli
from ibek.startup_cmds.commands import startup_cli
from ibek.support_cmds.commands import support_cli

from ._version import __version__

cli = typer.Typer()


cli.add_typer(
    support_cli,
    name="support",
    help="Commands for building support modules during container build",
)
cli.add_typer(
    ioc_cli,
    name="ioc",
    help="Commands for building generic IOCs during container build",
)
cli.add_typer(
    startup_cli,
    name="startup",
    help="Commands for building IOC instance startup files at container runtime",
)

yaml = YAML()


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@cli.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Print the version of ibek and exit",
    )
):
    """IOC Builder for EPICS and Kubernetes

    Provides support for building generic EPICS IOC container images and for
    running IOC instances in a Kubernetes cluster.
    """


# test with:
#     pipenv run python -m ibek
if __name__ == "__main__":
    cli()
