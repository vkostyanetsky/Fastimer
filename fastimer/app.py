#!/usr/bin/env python3

"""
This file contains the entry point of the application.
"""

import datetime
import os
import sys
from sys import stdout

import click
from vkostyanetsky import cliutils  # type: ignore

from fastimer import constants, datafile, statistics, utils
from fastimer.browser import FastsBrowser
from fastimer.commands import command_show, command_start
from fastimer.menu import FastimerMenu


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
    stdout.reconfigure(encoding=constants.ENCODING)


@cli.command(help="Start a new fast.")
@click.option("-p", "--path", type=__path_type(), help=__path_help())
def start(path: str | None) -> None:
    path = __get_path(path)
    command_start.main(path)


@cli.command(help="Show fasts by date.")
@click.option("-p", "--path", type=__path_type(), help=__path_help())
def show(path: str | None) -> None:
    path = __get_path(path)
    command_show.main(path)


# @cli.command(help="Check that data files have no mistakes.")
# @click.option("-p", "--path", type=__path_type(), help=__path_help())
# def test(path: str | None) -> None:
#     path = __get_path(path)
#     command_test.main(path)
#
#
# @cli.command(help="Set alarm according to notification settings.")
# @click.option("-p", "--path", type=__path_type(), help=__path_help())
# def beep(path: str | None):
#     path = __get_path(path)
#     command_beep.main(path)


# @cli.command(help="Display tasks for a given day (or days).")
# @click.argument(
#     "period", default="today", type=click.Choice(["today", "last", "next", "date"])
# )
# @click.argument("value", default="")
# @click.option("-p", "--path", type=__path_type(), help=__path_help())
# @click.option(
#     "-t", "--timesheet", is_flag=True, help="Show only tasks with time logged."
# )
# @click.option("-l", "--logs", is_flag=True, help="Show time logged for each task.")
# def show(path: str | None, timesheet: bool, logs: bool, period: str, value: str):
#     path = __get_path(path)
#     command_show.main(period, value, path, timesheet, logs)


if __name__ == "__main__":
    cli()
