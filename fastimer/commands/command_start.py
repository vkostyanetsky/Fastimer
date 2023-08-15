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
        new_fast = {
            "length": length,
            "started": datetime.datetime.now(),
        }

        fasts.append(new_fast)
        datafile.write_fasts(path, fasts)

        click.echo("Done! A new fast has been started.")
        utils.echo(new_fast)
