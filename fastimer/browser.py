#!/usr/bin/env python3

import datetime

from .utils import (
    aligned_string,
    get_time_difference,
    is_fast_completed,
    is_fast_stopped
)


def get_fast_description(fast: dict, include_zones: bool = False) -> list:
    now = datetime.datetime.now()
    goal = fast["started"] + datetime.timedelta(hours=fast["length"])

    description = [
        __get_fast_title(fast),
        "",
        __get_fast_from(fast),
        __get_fast_goal(fast, goal),
        ""
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
    value = "{goal} ({length} hours)".format(
        goal=goal.strftime("%a, %H:%M"), length=fast["length"]
    )

    return aligned_string("Goal", value, 5)


def __get_fast_elapsed_time(fast: dict, now: datetime.datetime) -> str:
    date1 = fast["started"]
    date2 = now if fast.get("stopped") is None else fast.get("stopped")

    value = __get_time_difference(date1, date2)

    return aligned_string("Elapsed time", value, 15)


def __get_fast_extra_time(now: datetime.datetime, goal: datetime.datetime) -> str:
    value = __get_time_difference(goal, now) if now >= goal else None

    return aligned_string("Extra time: ", value, 15)


def __get_fast_remaining_time(now: datetime.datetime, goal: datetime.datetime) -> str:
    value = (
        __get_time_difference(now - datetime.timedelta(minutes=1), goal)
        if now < goal
        else None
    )

    return aligned_string("Remaining", value, 15)


def __include_fasting_zones(description: list, fast: dict) -> None:
    description.append("Fasting zones:")
    description.append("")

    anabolic_zone = fast["started"]
    catabolic_zone = anabolic_zone + datetime.timedelta(hours=4)
    fat_burning_zone = catabolic_zone + datetime.timedelta(hours=12)
    ketosis_zone = fat_burning_zone + datetime.timedelta(hours=8)
    deep_ketosis_zone = ketosis_zone + datetime.timedelta(hours=48)

    now = datetime.datetime.now()
    fmt = "from %a, %H:%M"
    note = " <-- you are here"

    anabolic_zone_from = anabolic_zone.strftime(fmt)
    anabolic_zone_note = note if anabolic_zone <= now < catabolic_zone else ""
    anabolic_zone_info = "{}{}".format(anabolic_zone_from, anabolic_zone_note)

    catabolic_zone_from = catabolic_zone.strftime(fmt)
    catabolic_zone_note = note if catabolic_zone <= now < fat_burning_zone else ""
    catabolic_zone_info = "{}{}".format(catabolic_zone_from, catabolic_zone_note)

    fat_burning_zone_from = fat_burning_zone.strftime(fmt)
    fat_burning_zone_note = note if fat_burning_zone <= now < ketosis_zone else ""
    fat_burning_zone_info = "{}{}".format(fat_burning_zone_from, fat_burning_zone_note)

    ketosis_zone_from = ketosis_zone.strftime(fmt)
    ketosis_zone_note = note if ketosis_zone <= now < deep_ketosis_zone else ""
    ketosis_zone_info = "{}{}".format(ketosis_zone_from, ketosis_zone_note)

    deep_ketosis_zone_from = deep_ketosis_zone.strftime(fmt)
    deep_ketosis_zone_note = note if deep_ketosis_zone <= now else ""
    deep_ketosis_zone_info = "{}{}".format(
        deep_ketosis_zone_from, deep_ketosis_zone_note
    )

    description.append(aligned_string("- Anabolic", anabolic_zone_info))
    description.append(aligned_string("- Catabolic", catabolic_zone_info))
    description.append(aligned_string("- Fat burning", fat_burning_zone_info))
    description.append(aligned_string("- Ketosis", ketosis_zone_info))
    description.append(aligned_string("- Deep ketosis", deep_ketosis_zone_info))


def __get_fast_progress_bar(fast: dict, goal: datetime.datetime) -> str:
    seconds_now = (datetime.datetime.now() - fast["started"]).total_seconds()
    seconds_all = (goal - fast["started"]).total_seconds()

    percent = round(seconds_now / seconds_all * 100, 1)

    done_len = int(percent // 2.5)

    if done_len > 40:
        done_len = 40

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
