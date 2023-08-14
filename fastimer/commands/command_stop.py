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
        fasts[-1]["stopped"] = datetime.datetime.now()
        datafile.write_fasts(path, fasts)

        fast = fasts[len(fasts) - 1]

        utils.echo(fast)

    else:
        click.echo("No active fast to stop!")
