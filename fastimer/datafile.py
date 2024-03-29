#!/usr/bin/env python3

"""
Method to work with the fasts journal.
"""

import os
import typing

from yaml import parser, safe_dump, safe_load


def read_fasts(path: str) -> list[dict[str, typing.Any]]:
    """
    Reads the fasts journal.
    """

    yaml_file_name = os.path.join(path, __get_file_name())

    fasts = []

    if os.path.isfile(yaml_file_name):
        try:
            with open(yaml_file_name, encoding="utf-8-sig") as yaml_file:
                fasts = safe_load(yaml_file)

        except parser.ParserError:
            print(f"Unable to parse: {yaml_file_name}")

    return fasts


def write_fasts(path: str, fasts: list[dict[str, typing.Any]]) -> None:
    """
    Writes the fasts journal.
    """

    for fast in fasts:
        fast["started"] = fast["started"].replace(microsecond=0)

        if fast.get("stopped") is not None:
            fast["stopped"] = fast["stopped"].replace(microsecond=0)

    yaml_file_name = os.path.join(path, __get_file_name())

    with open(yaml_file_name, encoding="utf-8-sig", mode="w") as yaml_file:
        safe_dump(fasts, yaml_file)


def __get_file_name() -> str:
    return "fasts.yaml"
