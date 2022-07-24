#!/usr/bin/env python3

import datetime

from .utils import get_time_difference


def display_fast(fast: dict) -> None:
    goal = fast["started"] + datetime.timedelta(hours=fast["length"])

    elapsed_time = __get_elapsed_time(fast)
    time_now = datetime.datetime.now()

    if time_now < goal:
        time = __get_time(time_now, goal)
        time = f"Remaining:       {time}"
    else:
        time = __get_time(goal, time_now)
        time = f"Excess time:     {time}"

    started = fast["started"].strftime("%a, %H:%M")

    goal = goal.strftime("%a, %H:%M")

    print(f"Started:  {started}")
    print(f'Goal:     {goal} ({fast["length"]} hours)')
    print()
    print(f"Elapsed time:    {elapsed_time}")
    print(time)


def __get_time(start_date: datetime, end_date: datetime) -> str:

    hours, minutes = get_time_difference(start_date, end_date)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)

    return f"{hours}:{minutes}"


def __get_elapsed_time(fast: dict) -> str:
    date1 = fast["started"]
    date2 = datetime.datetime.today() if fast["stopped"] is None else fast["stopped"]

    return __get_time(date1, date2)
