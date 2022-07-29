#!/usr/bin/env python3

import datetime

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .utils import get_time_difference, print_with_alignment


def show_fast(prompt: PromptUtils, fasts: list, active_fast: dict) -> None:

    print("ACTIVE FAST")
    print()

    now = datetime.datetime.now()
    goal = active_fast["started"] + datetime.timedelta(hours=active_fast["length"])
    is_completed = active_fast.get("stopped") is not None

    __print_fast_started(active_fast)
    __print_fast_goal(active_fast, goal)

    print()

    __print_fast_zones(active_fast)

    print()

    __print_fast_elapsed_time(active_fast, now)

    if now > goal:
        __print_fast_extra_time(goal, now)
    else:
        __print_fast_remaining_time(goal, now)

    print()

    __print_fast_progress_bar(active_fast, goal)

    if is_completed:
        print()
        print("Well done! You have completed your goal!")

    print()
    prompt.enter_to_continue()


def __print_fast_started(fast: dict) -> None:

    value = __get_day(fast["started"])

    print_with_alignment("Started", value)


def __print_fast_goal(fast: dict, goal: datetime.datetime) -> None:

    value = "{goal} ({length} hours)".format(
        goal=goal.strftime("%a, %H:%M"), length=fast["length"]
    )

    print_with_alignment("Goal", value)


def __print_fast_zones(fast: dict) -> None:

    print("Fasting zones:")
    print()

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

    print_with_alignment("- Anabolic", anabolic_zone_info)
    print_with_alignment("- Catabolic", catabolic_zone_info)
    print_with_alignment("- Fat burning", fat_burning_zone_info)
    print_with_alignment("- Ketosis", ketosis_zone_info)
    print_with_alignment("- Deep ketosis", deep_ketosis_zone_info)


def __print_fast_elapsed_time(fast: dict, now: datetime.datetime) -> None:

    date1 = fast["started"]
    date2 = now if fast.get("stopped") is None else fast.get("stopped")

    value = __get_time_difference(date1, date2)

    print_with_alignment("Elapsed time", value)


def __print_fast_extra_time(goal: datetime.datetime, now: datetime.datetime) -> None:

    value = __get_time_difference(goal, now) if now >= goal else None

    print_with_alignment("Extra time", value)


def __print_fast_remaining_time(
    goal: datetime.datetime, now: datetime.datetime
) -> None:

    value = (
        __get_time_difference(now - datetime.timedelta(minutes=1), goal)
        if now < goal
        else None
    )

    print_with_alignment("Remaining", value)


def __print_fast_progress_bar(fast: dict, goal: datetime.datetime) -> None:

    seconds_now = (datetime.datetime.now() - fast["started"]).total_seconds()
    seconds_all = (goal - fast["started"]).total_seconds()

    percent = round(seconds_now / seconds_all * 100, 1)

    done_len = int(percent // 2.5)

    if done_len > 40:
        done_len = 40

    left_len = int(40 - done_len)

    bar = "| {done}{left} | {tail}%".format(
        done="#" * done_len, left="-" * left_len, tail=str(percent)
    )

    print(bar)


def __get_time_difference(start_date: datetime, end_date: datetime) -> str:

    hours, minutes = get_time_difference(start_date, end_date)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)

    return f"{hours}:{minutes}"


def __get_day(date: datetime.datetime) -> str:

    return date.strftime("%a, %H:%M")