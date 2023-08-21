#!/usr/bin/env python3

"""Implementation of a command to output a fast."""

import typing

import click

from fastimer import datafile, utils


def main(path: str, what: str | None) -> None:
    """
    Outputs a detailed view of a fast.
    """

    fasts = datafile.read_fasts(path)

    if fasts:
        if what == "last":
            __show_last(fasts)
        elif what == "prev":
            __show_prev(fasts)

    else:
        click.echo("Nothing to show, since there are no recorded fasts.")


def __show_last(fasts: list[dict[str, typing.Any]]) -> None:
    utils.print_fast(fasts[-1])


def __show_prev(fasts: list[dict[str, typing.Any]]) -> None:
    if len(fasts) >= 2:
        utils.print_fast(fasts[-2])
    else:
        click.echo("Nothing to show, since there is no previous fast.")
