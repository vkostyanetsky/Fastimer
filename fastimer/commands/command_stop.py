#!/usr/bin/env python3

"""Implementation of a command to stop an ongoing fast."""

import datetime

import click

from fastimer import datafile, utils


def main(path: str) -> None:
    """
    Finishes the active fast.
    """

    fasts = datafile.read_fasts(path)

    if utils.get_active_fast(fasts) is not None:
        fast = fasts[-1]

        fast["stopped"] = datetime.datetime.now()
        datafile.write_fasts(path, fasts)

        click.echo(
            click.style(text="Done! The active fast has been stopped.", fg="green")
        )
        click.echo()

        utils.print_fast(fast)

    else:
        click.echo("No active fast to stop!")
