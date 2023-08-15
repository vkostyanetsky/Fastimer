#!/usr/bin/env python3

"""Implementation of a command to cancel an ongoing fast."""

import click

from fastimer import datafile, utils


def main(path: str) -> None:
    """
    Cancels the active fast.
    """

    fasts = datafile.read_fasts(path)
    fast = utils.get_active_fast(fasts)

    if fast is not None:
        fasts.remove(fast)
        datafile.write_fasts(path, fasts)

        click.echo(
            click.style(text="Done! The active fast has been cancelled.", fg="green")
        )

    else:
        click.echo("No active fast to cancel!")
