#!/usr/bin/env python3

"""
This file contains the entry point of the application.
"""

import os
from sys import stdout

import click

from fastimer import constants
from fastimer.commands import command_show, command_start


def __get_path(path: str | None) -> str:
    """
    Determines the path to a working directory. It is supposed to be the "Fastimer" folder
    in user's home directory in case it's not specified via app's options.
    """

    if path is None:
        path = os.path.expanduser("~")
        path = os.path.join(path, "Fastimer")

    return path


def __path_help() -> str:
    return "Set path to working directory."


def __path_type() -> click.Path:
    return click.Path(exists=True)


@click.group(help="CLI tool that helps with fasting.")
def cli():
    """
    Main entry point.
    """

    stdout.reconfigure(encoding=constants.ENCODING)


@cli.command(help="Start a new fast.")
@click.option("-p", "--path", type=__path_type(), help=__path_help())
def start(path: str | None) -> None:
    """
    Creates a new fast entry in the data file.
    """

    path = __get_path(path)
    command_start.main(path)


@cli.command(help="Show fasts by date.")
@click.option("-p", "--path", type=__path_type(), help=__path_help())
def show(path: str | None) -> None:
    """
    Outputs detailed information about a fast.
    """

    path = __get_path(path)
    command_show.main(path)


if __name__ == "__main__":
    cli()
