#!/usr/bin/env python3

"""Implementation of a command to output a fast."""

from fastimer import datafile, utils


def main(path: str) -> None:
    """
    Outputs a detailed view of a fast.
    """

    fasts = datafile.read_fasts(path)
    fast = fasts[len(fasts) - 1]

    utils.echo(fast)
