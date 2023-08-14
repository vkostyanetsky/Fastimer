#!/usr/bin/env python3

"""
Implementation of a command to output a fast.
"""

import datetime
import typing

import click

from fastimer import datafile, utils


def main(path: str) -> None:
    """
    Generates a detailed view of a fast.
    """

    fasts = datafile.read_fasts(path)
    index = len(fasts) - 1
    fast = fasts[index]

    time = fast["stopped"] if utils.is_fast_stopped(fast) else datetime.datetime.now()

    goal = fast["started"] + datetime.timedelta(hours=fast["length"])

    __echo_fast_title(fast)
    click.echo()

    __echo_fast_from(fast)
    __echo_fast_goal(fast, goal)
    click.echo()

    __echo_fasting_zones(fast, time)
    click.echo()

    __echo_fast_progress_bar(fast, goal, time)
    click.echo()

    __echo_fast_elapsed_time(fast, time)

    if time <= goal:
        __echo_fast_remaining_time(time, goal)
    else:
        __echo_fast_extra_time(time, goal)


def __echo_fast_title(fast: dict[str, typing.Any]) -> None:
    if utils.is_fast_stopped(fast):
        if utils.is_fast_completed(fast):
            click.echo(click.style(text="COMPLETED FAST", fg="green"))
        else:
            click.echo(click.style(text="FAILED FAST", fg="red"))
    else:
        click.echo(click.style(text="ACTIVE FAST", fg="yellow"))


def __echo_fast_from(fast: dict[str, typing.Any]) -> None:
    value = __get_day(fast["started"])
    value = utils.title_and_value("From", value, 5)

    click.echo(value)


def __echo_fast_goal(fast: dict[str, typing.Any], goal: datetime.datetime) -> None:
    length = fast["length"]
    goal_string = __get_day(goal)
    goal_string = f"{goal_string} ({length} hours)"
    goal_string = utils.title_and_value("Goal", goal_string, 5)

    click.echo(goal_string)


def __echo_fast_elapsed_time(
    fast: dict[str, typing.Any], time: datetime.datetime
) -> None:
    date1 = fast["started"]
    date2 = time if fast.get("stopped") is None else fast["stopped"]

    value = __get_time_difference(date1, date2)
    value = utils.title_and_value("Elapsed time", value, 15)

    click.echo(str(value))


def __echo_fast_extra_time(time: datetime.datetime, goal: datetime.datetime) -> None:
    value = __get_time_difference(goal, time) if time >= goal else None
    value = utils.title_and_value("Extra time", value, 15)

    click.echo(str(value))


def __echo_fast_remaining_time(
    time: datetime.datetime, goal: datetime.datetime
) -> None:
    value = (
        __get_time_difference(time - datetime.timedelta(minutes=1), goal)
        if time < goal
        else None
    )

    value = utils.title_and_value("Remaining", value, 15)

    click.echo(str(value))


def __line_for_zone(
    note: str,
    time: datetime.datetime,
    title: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime | None,
) -> str:
    zone_from = f"from {__get_day(start_time)}"

    if end_time is None:
        zone_note = note if start_time <= time else ""
    else:
        zone_note = note if start_time <= time < end_time else ""

    zone_note = utils.title_and_value(f"- {title}", f"{zone_from}{zone_note}")

    return str(zone_note)


def __echo_fasting_zones(fast: dict[str, typing.Any], time: datetime.datetime) -> None:
    note = " <-- you were here" if utils.is_fast_stopped(fast) else " <-- you are here"

    anabolic_zone = fast["started"]
    catabolic_zone = anabolic_zone + datetime.timedelta(hours=4)
    fat_burning_zone = catabolic_zone + datetime.timedelta(hours=12)
    ketosis_zone = fat_burning_zone + datetime.timedelta(hours=8)
    deep_ketosis_zone = ketosis_zone + datetime.timedelta(hours=48)

    click.echo("Fasting zones:")
    click.echo("")

    line = __line_for_zone(note, time, "Anabolic", anabolic_zone, catabolic_zone)
    click.echo(line)

    line = __line_for_zone(note, time, "Catabolic", catabolic_zone, fat_burning_zone)
    click.echo(line)

    line = __line_for_zone(note, time, "Fat burning", fat_burning_zone, ketosis_zone)
    click.echo(line)

    line = __line_for_zone(note, time, "Ketosis", ketosis_zone, deep_ketosis_zone)
    click.echo(line)

    line = __line_for_zone(note, time, "Anabolic", deep_ketosis_zone, None)
    click.echo(line)


def __echo_fast_progress_bar(
    fast: dict[str, typing.Any], goal: datetime.datetime, time: datetime.datetime
) -> None:
    seconds_now = (time - fast["started"]).total_seconds()
    seconds_all = (goal - fast["started"]).total_seconds()

    percent = round(seconds_now / seconds_all * 100, 1)

    done_len = int(percent // 2.5)
    done_len = min(done_len, 40)

    left_len = int(40 - done_len)

    left = "-" * left_len
    done = "#" * done_len
    tail = str(percent)

    click.echo(f"{done}{left} {tail}%")


def __get_time_difference(
    start_date: datetime.datetime, end_date: datetime.datetime
) -> str:
    hours, minutes = utils.get_time_difference(start_date, end_date)

    hours_string = str(hours).zfill(2)
    minutes_string = str(minutes).zfill(2)

    return f"{hours_string}h {minutes_string}m"


def __get_day(date: datetime.datetime) -> str:
    if (datetime.datetime.now() - date).days > 7:
        fmt = "%Y-%m-%d %H:%M"
    else:
        fmt = "%a, %H:%M"

    return date.strftime(fmt)
