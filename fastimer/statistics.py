#!/usr/bin/env python3
import datetime
from collections import namedtuple
from .utils import get_time_difference


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

    print("Completed Fasts:       {}".format(len(data.journal)))

    print(
        "Total Fasting Time:    {hours}h {minutes}m".format(
            hours=int(total_hours), minutes=int(total_minutes)
        )
    )
    print("Average Fast Length:   {hours}h".format(hours=int(avg_fast_length)))

    print()
