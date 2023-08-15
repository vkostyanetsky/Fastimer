#!/usr/bin/env python3

"""Implementation of a command to output a fast."""

from fastimer import datafile, utils


def main(path: str, what: str, value: str) -> None:
    """
    Outputs a detailed view of a fast.
    """

    fasts = datafile.read_fasts(path)

    if what == "today":
        __show_today(fasts)
    elif what == "last":
        pass
        # __show_last_n_fasts(
        #     tasks, plans, state, int(value) if value else 1, timesheet, logs
        # )
    elif what == "date":
        pass
        # __show_date(tasks, plans, state, value, timesheet, logs)


def __show_today(fasts) -> None:
    utils.print_fast(fasts[-1])
