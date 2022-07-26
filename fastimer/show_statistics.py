#!/usr/bin/env python3

import datetime

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .fasts_file import read_fasts
from .utils import get_time_difference, print_with_alignment


def show_statistics(prompt_utils: PromptUtils) -> None:

    fasts = read_fasts()

    total_hours, total_minutes = __get_total_hours_and_minutes(fasts)

    completed_fasts = str(len(fasts))
    total_fasting_time = "{hours}h {minutes}m".format(
        hours=int(total_hours), minutes=int(total_minutes)
    )
    average_fast_length = __get_average_fast_length(fasts, total_hours, total_minutes)

    offset = 22

    print_with_alignment("Completed Fasts", completed_fasts, offset)
    print_with_alignment("Total Fasting Time", total_fasting_time, offset)
    print_with_alignment("Average Fast Length", average_fast_length, offset)

    print()
    prompt_utils.enter_to_continue()


def __get_total_hours_and_minutes(fasts: list) -> tuple:

    total_hours = 0
    total_minutes = 0

    for fast in fasts:
        started = fast["started"]
        stopped = (
            fast.get("stopped")
            if fast.get("stopped") is not None
            else datetime.datetime.now()
        )

        hours, minutes = get_time_difference(started, stopped)

        total_hours += hours
        total_minutes += minutes

    minutes_per_hour = 60

    if total_minutes >= minutes_per_hour:
        hours = total_minutes // minutes_per_hour
        total_minutes = total_minutes % minutes_per_hour
        total_hours += hours

    return total_hours, total_minutes


def __get_average_fast_length(fasts: list, hours_total: int, minutes_total: int) -> str:

    fasts_total = len(fasts)
    minutes_per_hour = 60

    avg_fast_length = (
        (hours_total * 60 + minutes_total) / fasts_total // minutes_per_hour
    )

    return "{hours}h".format(hours=int(avg_fast_length))
