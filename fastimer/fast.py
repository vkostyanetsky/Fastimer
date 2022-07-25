#!/usr/bin/env python3

import datetime

from .utils import get_time_difference


def display_fast(fast: dict) -> None:
    goal = fast["started"] + datetime.timedelta(hours=fast["length"])

    elapsed_time = __get_elapsed_time(fast)
    time_now = datetime.datetime.now()

    if time_now < goal:
        remaining_time = __get_time(time_now, goal)
        excess_time = None
    else:
        remaining_time = "00:00"
        excess_time = __get_time(goal, time_now)

    started = fast["started"].strftime("%a, %H:%M")

    goal = goal.strftime("%a, %H:%M")

    __print_with_alignment("Started", started)
    __print_with_alignment("Goal", f'{goal} ({fast["length"]} hours)')

    print()

    __print_with_alignment("Elapsed time", elapsed_time)
    __print_with_alignment("Remaining", remaining_time)

    if excess_time is not None:
        print()
        print("You have completed your fast!")
        print()
        __print_with_alignment("Excess time", excess_time)


def __print_with_alignment(title: str, value: str) -> None:
    title = f"{title}:".ljust(15)
    string = "{} {}".format(title, value)

    print(string)

def __get_time(start_date: datetime, end_date: datetime) -> str:

    hours, minutes = get_time_difference(start_date, end_date)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)

    return f"{hours}:{minutes}"


def __get_elapsed_time(fast: dict) -> str:
    date1 = fast["started"]
    date2 = datetime.datetime.today() if fast["stopped"] is None else fast["stopped"]

    return __get_time(date1, date2)
