#!/usr/bin/env python3

import datetime

from .utils import get_time_difference


def display_fast(fast: dict) -> None:

    print("ACTIVE FAST")
    print()

    goal = fast["started"] + datetime.timedelta(hours=fast["length"])

    elapsed_time = __get_elapsed_time(fast)
    time_now = datetime.datetime.now()

    if time_now < goal:
        remaining_time = __get_time(time_now, goal)
        extra_time = None
    else:
        remaining_time = "00:00"
        extra_time = __get_time(goal, time_now)

    started = fast["started"].strftime("%a, %H:%M")

    goal_as_string = goal.strftime("%a, %H:%M")

    __print_with_alignment("Started", started)
    __print_with_alignment("Goal", f'{goal_as_string} ({fast["length"]} hours)')

    print()

    __print_with_alignment("Elapsed time", elapsed_time)

    if extra_time is None:
        __print_with_alignment("Remaining", remaining_time)
    else:
        __print_with_alignment("Extra time", extra_time)

    print()

    __print_progress_bar(fast, goal)

    if extra_time is not None:
        print()
        print("Well done! You have completed your goal!")


def __print_with_alignment(title: str, value: str) -> None:
    title = f"{title}:".ljust(15)
    string = "{} {}".format(title, value)

    print(string)


def __print_progress_bar(fast: dict, goal: datetime.datetime) -> None:

    seconds_now = (datetime.datetime.now() - fast["started"]).total_seconds()
    seconds_all = (goal-fast["started"]).total_seconds()

    percent = round(seconds_now / seconds_all * 100, 1)

    done_len = int(percent // 2.5)

    if done_len > 40:
        done_len = 40

    left_len = int(40 - done_len)

    bar = "| {done}{left} | {tail}%".format(done="#" * done_len, left="-" * left_len, tail=str(percent))

    print(bar)


def __get_time(start_date: datetime, end_date: datetime) -> str:

    hours, minutes = get_time_difference(start_date, end_date)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)

    return f"{hours}:{minutes}"


def __get_elapsed_time(fast: dict) -> str:
    date1 = fast["started"]
    date2 = datetime.datetime.today() if fast.get("stopped") is None else fast.get("stopped")

    return __get_time(date1, date2)
