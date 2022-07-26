#!/usr/bin/env python3

import datetime

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .fasts_file import read_fasts
from .utils import get_active_fast, get_time_difference, print_with_alignment


def show_fast(prompt: PromptUtils) -> None:

    fasts = read_fasts()
    fast = get_active_fast(fasts)

    if fast is None:
        print("No current fast to display.")
    else:
        __print_fast(fast)

    print()
    prompt.enter_to_continue()


def __print_fast(fast: dict) -> None:

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

    print_with_alignment("Started", started)
    print_with_alignment("Goal", f'{goal_as_string} ({fast["length"]} hours)')

    print()

    __print_fasting_zones(fast)

    print()

    print_with_alignment("Elapsed time", elapsed_time)

    if extra_time is None:
        print_with_alignment("Remaining", remaining_time)
    else:
        print_with_alignment("Extra time", extra_time)

    print()

    __print_progress_bar(fast, goal)

    if extra_time is not None:
        print()
        print("Well done! You have completed your goal!")


def __print_fasting_zones(fast: dict) -> None:

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


def __print_progress_bar(fast: dict, goal: datetime.datetime) -> None:

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


def __get_time(start_date: datetime, end_date: datetime) -> str:

    hours, minutes = get_time_difference(start_date, end_date)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)

    return f"{hours}:{minutes}"


def __get_elapsed_time(fast: dict) -> str:

    date1 = fast["started"]
    date2 = (
        datetime.datetime.today()
        if fast.get("stopped") is None
        else fast.get("stopped")
    )

    return __get_time(date1, date2)
