#!/usr/bin/env python3

"""Implementation of a command to start a new fast."""

import datetime

import click

from fastimer import datafile, utils


def main(path: str, length: int) -> None:
    """
    Starts a new fast.
    """

    fasts = datafile.read_fasts(path)
    fast = utils.get_active_fast(fasts)

    if fast is not None:
        click.echo("Fast is already on.")

    else:
        fast = {
            "length": length,
            "started": datetime.datetime.now(),
        }

        fasts.append(fast)

        datafile.write_fasts(path, fasts)

        fast = fasts[len(fasts) - 1]

        utils.echo(fast)
