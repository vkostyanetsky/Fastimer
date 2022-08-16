#!/usr/bin/env python3

import datetime

from .utils import (
    aligned_string,
    get_time_difference,
    is_fast_completed,
    is_fast_stopped,
)


def get(fast: dict, include_zones: bool = False) -> list:
    now = datetime.datetime.now()
    goal = fast["started"] + datetime.timedelta(hours=fast["length"])

    description = [
        __get_fast_title(fast),
        "",
        __get_fast_from(fast),
        __get_fast_goal(fast, goal),
        "",
    ]

    if include_zones:
        __include_fasting_zones(description, fast)
        description.append("")

    description.append(__get_fast_progress_bar(fast, goal))

    description.append("")

    description.append(__get_fast_elapsed_time(fast, now))

    if now <= goal:
        description.append(__get_fast_remaining_time(now, goal))
    else:
        description.append(__get_fast_extra_time(now, goal))

    if is_fast_completed(fast):
        description.append("")
        description.append("Well done! You have completed this fast!")

    return description


def __get_fast_title(fast: dict) -> str:

    if is_fast_stopped(fast):
        title = "COMPLETED FAST" if is_fast_completed(fast) else "FAILED FAST"
    else:
        title = "ACTIVE FAST"

    return title


def __get_fast_from(fast: dict) -> str:
    value = __get_day(fast["started"])

    return aligned_string("From", value, 5)


def __get_fast_goal(fast: dict, goal: datetime.datetime) -> str:

    goal = goal.strftime("%a, %H:%M")
    length = fast["length"]
    goal_string = f"{goal} ({length} hours)"

    return aligned_string("Goal", goal_string, 5)


def __get_fast_elapsed_time(fast: dict, now: datetime.datetime) -> str:
    date1 = fast["started"]
    date2 = now if fast.get("stopped") is None else fast.get("stopped")

    value = __get_time_difference(date1, date2)

    return aligned_string("Elapsed time", value, 15)


def __get_fast_extra_time(now: datetime.datetime, goal: datetime.datetime) -> str:
    value = __get_time_difference(goal, now) if now >= goal else None

    return aligned_string("Extra time", value, 15)


def __get_fast_remaining_time(now: datetime.datetime, goal: datetime.datetime) -> str:
    value = (
        __get_time_difference(now - datetime.timedelta(minutes=1), goal)
        if now < goal
        else None
    )

    return aligned_string("Remaining", value, 15)


def __include_fasting_zones(lines: list, fast: dict) -> None:
    def add_line_for_zone(title, start_time, end_time=None) -> None:

        zone_from = start_time.strftime("from %a, %H:%M")
        note = " <-- you are here"

        if end_time is None:
            zone_note = note if start_time <= now else ""
        else:
            zone_note = note if start_time <= now < end_time else ""

        zone_info = aligned_string(f"- {title}", f"{zone_from}{zone_note}")

        lines.append(zone_info)

    anabolic_zone = fast["started"]
    catabolic_zone = anabolic_zone + datetime.timedelta(hours=4)
    fat_burning_zone = catabolic_zone + datetime.timedelta(hours=12)
    ketosis_zone = fat_burning_zone + datetime.timedelta(hours=8)
    deep_ketosis_zone = ketosis_zone + datetime.timedelta(hours=48)

    now = datetime.datetime.now()

    lines.append("Fasting zones:")
    lines.append("")

    add_line_for_zone("Anabolic", anabolic_zone, catabolic_zone)
    add_line_for_zone("Catabolic", catabolic_zone, fat_burning_zone)
    add_line_for_zone("Fat burning", fat_burning_zone, ketosis_zone)
    add_line_for_zone("Ketosis", ketosis_zone, deep_ketosis_zone)
    add_line_for_zone("Anabolic", deep_ketosis_zone)


def __get_fast_progress_bar(fast: dict, goal: datetime.datetime) -> str:
    seconds_now = (datetime.datetime.now() - fast["started"]).total_seconds()
    seconds_all = (goal - fast["started"]).total_seconds()

    percent = round(seconds_now / seconds_all * 100, 1)

    done_len = int(percent // 2.5)
    done_len = min(done_len, 40)

    left_len = int(40 - done_len)

    left = "-" * left_len
    done = "#" * done_len
    tail = str(percent)

    return f"{done}{left} {tail}%"


def __get_time_difference(start_date: datetime, end_date: datetime) -> str:
    hours, minutes = get_time_difference(start_date, end_date)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)

    return f"{hours}h {minutes}m"


def __get_day(date: datetime.datetime) -> str:
    return date.strftime("%a, %H:%M")
