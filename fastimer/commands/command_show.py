#!/usr/bin/env python3

"""Implementation of a command to output a fast."""
import click

from fastimer import datafile, utils


def main(path: str, what: str, date: str) -> None:
    """
    Outputs a detailed view of a fast.
    """

    fasts = datafile.read_fasts(path)

    if fasts:
        if what == "last":
            __show_last(fasts)
        elif what == "prev":
            __show_prev(fasts)
        elif what == "on":
            pass
            __show_on(fasts, date)

    else:
        click.echo("Nothing to show, since there are no recorded fasts.")


def __show_last(fasts) -> None:
    utils.print_fast(fasts[-1])


def __show_prev(fasts) -> None:
    if len(fasts) >= 2:
        utils.print_fast(fasts[-2])
    else:
        click.echo("Nothing to show, since there is no previous fast.")


def __show_on(fasts, date) -> None:
    pass
