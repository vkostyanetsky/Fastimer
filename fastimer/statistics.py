#!/usr/bin/env python3
import datetime
from collections import namedtuple
from .utils import get_time_difference, __print_with_alignment


def print_statistics(data: namedtuple) -> None:

    total_hours = 0
    total_minutes = 0

    for fast in data.journal:
        started = fast["started"]
        stopped = (
            fast.get("stopped") if fast.get("stopped") is not None else datetime.datetime.now()
        )

        hours, minutes = get_time_difference(started, stopped)

        total_hours += hours
        total_minutes += minutes

    minutes_per_hour = 60

    if total_minutes >= minutes_per_hour:
        hours = total_minutes // minutes_per_hour
        total_minutes = total_minutes % minutes_per_hour
        total_hours += hours

    avg_fast_length = (total_hours * 60 + total_minutes) / len(data.journal) // 60

    completed_fasts = str(len(data.journal))
    total_fasting_time = "{hours}h {minutes}m".format(hours=int(total_hours), minutes=int(total_minutes))
    average_fast_length = "{hours}h".format(hours=int(avg_fast_length))

    __print_with_alignment("Completed Fasts", completed_fasts, 22)
    __print_with_alignment("Total Fasting Time", total_fasting_time, 22)
    __print_with_alignment("Average Fast Length", average_fast_length, 22)

    print()
