#!/usr/bin/env python3

import datetime

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .fasts_file import read_fasts
from .utils import get_time_difference, print_with_alignment


def show_statistics(prompt_utils: PromptUtils) -> None:

    fasts = read_fasts()

    print("FASTING STATISTICS")
    print()

    __print_completed_fasts(fasts)
    __print_incomplete_fasts(fasts)
    __print_total_fasting_time(fasts)
    __print_average_fast_length(fasts)
    __print_longest_fast_length(fasts)
    __print_longest_fasting_streak(fasts)
    __print_current_fasting_streak(fasts)
    print()

    __print_achievements(fasts)
    print()

    prompt_utils.enter_to_continue()


def __print_completed_fasts(fasts: list) -> None:

    value = __get_number_of_completed_fasts(fasts)
    value = str(value)

    __print_with_alignment("Completed Fasts", value)


def __print_incomplete_fasts(fasts: list) -> None:

    value = __get_number_of_incomplete_fasts(fasts)
    value = str(value)

    __print_with_alignment("Incomplete Fasts", value)


def __print_total_fasting_time(fasts: list) -> None:

    total_hours, total_minutes = __get_total_hours_and_minutes(fasts)

    value = __get_period_string(total_hours, total_minutes)

    __print_with_alignment("Total Fasting Time", value)


def __print_average_fast_length(fasts: list) -> None:

    hours_total, minutes_total = __get_total_hours_and_minutes(fasts)

    minutes_per_hour = 60

    fasts_total = __get_number_of_completed_fasts(fasts)
    all_minutes = hours_total * 60 + minutes_total
    avg_minutes = all_minutes / fasts_total

    avg_hours = avg_minutes // minutes_per_hour
    avg_minutes -= avg_hours * minutes_per_hour

    value = __get_period_string(avg_hours, avg_minutes)

    __print_with_alignment("Average Fast Length", value)


def __print_longest_fast_length(fasts: list) -> None:

    hours, minutes = __get_longest_fast_length(fasts)

    value = __get_period_string(hours, minutes)

    __print_with_alignment("Longest Fast Length", value)


def __print_longest_fasting_streak(fasts: list) -> None:

    value = __get_longest_fasting_streak(fasts)
    value = "{} days".format(value)

    __print_with_alignment("Longest Fasting Streak", value)


def __print_current_fasting_streak(fasts: list) -> None:

    value = __get_current_fasting_streak(fasts)
    value = "{} days".format(value)

    __print_with_alignment("Current Fasting Streak", value)


def __print_achievements(fasts: list) -> None:

    print("Achievements:")

    achievements = __get_achievements(fasts)

    if len(achievements) == 0:
        print("- Nothing yet.")
    else:
        for achievement in achievements:
            print("- {}".format(achievement))


def __print_with_alignment(title: str, value: str):

    print_with_alignment(title, value, 24)


def __get_achievements(fasts: list) -> list:

    result = []

    __add_completed_fasts_achievement(result, fasts)
    __add_longest_streak_achievement(result, fasts)
    __add_daily_fasting_achievement(result, fasts)

    return result


def __add_completed_fasts_achievement(achievements: list, fasts: list) -> None:

    completed_fasts = __get_number_of_completed_fasts(fasts)

    levels = {
        5: "WOODEN PERSISTENCE (level 1 badge out of 9). "
           "Five fasts completed!",
        25: "COPPER PERSISTENCE (level 2 badge out of 9). "
            "Twenty five fasts completed!",
        50: "BRONZE PERSISTENCE (level 3 badge out of 9). "
            "Fifty fasts completed!",
        100: "IRON PERSISTENCE (level 4 badge out of 9). "
             "One hundred fasts completed!",
        250: "STEEL PERSISTENCE (level 5 badge out of 9). "
             "Two hundred and fifty fasts completed!",
        500: "SILVER PERSISTENCE (level 6 badge out of 9). "
             "Five hundred fasts completed!",
        1000: "GOLD PERSISTENCE (level 7 badge out of 9). "
              "Thousand fasts completed!",
        2500: "PLATINUM PERSISTENCE (level 8 badge out of 9). "
              "Two and a half thousand fasts completed!",
        5000: "DIAMOND PERSISTENCE (level 9 badge out of 9). "
              "Five thousand fasts completed!"
    }

    __add_achievement(achievements, levels, completed_fasts)


def __add_longest_streak_achievement(achievements: list, fasts: list) -> None:

    longest_fasting_streak = __get_longest_fasting_streak(fasts)

    levels = {
        5: "WOODEN HABIT (level 1 badge out of 9). "
           "Five completed fasts in a row!",
        10: "COPPER HABIT (level 2 badge out of 9). "
            "Ten completed fasts in a row!",
        25: "BRONZE HABIT (level 3 badge out of 9). "
            "Twenty five completed fasts in a row!",
        50: "IRON HABIT (level 4 badge out of 9). "
            "Fifty completed fasts in a row!",
        100: "STEEL HABIT (level 5 badge out of 9). "
             "One hundred completed fasts in a row!",
        150: "SILVER HABIT (level 6 badge out of 9). "
             "One hundred and fifty completed fasts in a row!",
        200: "GOLD HABIT (level 7 badge out of 9). "
             "Two hundred completed fasts in a row!",
        250: "PLATINUM HABIT (level 8 badge out of 9). "
             "Two hundred and fifty completed fasts in a row!",
        365: "DIAMOND HABIT (level 9 badge out of 9). "
             "Three hundred sixty five completed fasts in a row!"
    }

    __add_achievement(achievements, levels, longest_fasting_streak)


def __add_daily_fasting_achievement(achievements: list, fasts: list) -> None:

    hours, _ = __get_longest_fast_length(fasts)

    levels = {
        24: "BRONZE ASCETIC (level 1 badge out of 3). "
            "Twenty four hours of continued fasting!",
        48: "IRON ASCETIC (level 2 badge out of 3). "
            "Forty eight hours of continued fasting!",
        72: "STEEL ASCETIC (level 3 badge out of 3). "
            "Seventy two hours of continued fasting!",
    }

    __add_achievement(achievements, levels, hours)


def __add_achievement(achievements: list, levels: dict, value: int) -> None:

    achievement = None

    for number_to_get in levels:
        if value >= number_to_get:
            achievement = levels[number_to_get]

    if achievement is not None:
        achievements.append(achievement)


def __get_period(date: datetime.datetime) -> tuple:

    period_from = date.replace(hour=0, minute=0, second=0, microsecond=0)
    period_to = period_from + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)

    return period_from, period_to


def __get_fast_length(fast: dict) -> tuple:

    started = fast["started"]
    stopped = fast.get("stopped")

    if stopped is not None:
        result = get_time_difference(started, stopped)
    else:
        result = 0, 0

    return result


def __get_total_hours_and_minutes(fasts: list) -> tuple:

    total_hours = 0
    total_minutes = 0

    for fast in fasts:

        hours, minutes = __get_fast_length(fast)

        total_hours += hours
        total_minutes += minutes

    minutes_per_hour = 60

    if total_minutes >= minutes_per_hour:
        hours = total_minutes // minutes_per_hour
        total_minutes = total_minutes % minutes_per_hour
        total_hours += hours

    return total_hours, total_minutes


def __get_number_of_completed_fasts(fasts: list) -> int:

    result = 0

    for fast in fasts:

        if fast.get("stopped") is None:
            continue

        if fast.get("length") > __get_fast_length(fast)[0]:
            continue

        result += 1

    return result


def __get_number_of_incomplete_fasts(fasts: list) -> int:

    result = 0

    for fast in fasts:

        if fast.get("stopped") is None:
            continue

        if fast.get("length") <= __get_fast_length(fast)[0]:
            continue

        result += 1

    return result


def __get_fasting_streaks(fasts: list) -> list:

    streaks = []
    current_streak = 0

    seconds_per_minute = 60
    minutes_per_hour = 60
    hours_per_day = 24
    seconds_per_day = seconds_per_minute * minutes_per_hour * hours_per_day

    if __get_number_of_completed_fasts(fasts) > 0:

        previous_fast = None

        for fast in fasts:

            if fast.get("stopped") is None:
                continue

            if fast.get("length") > __get_fast_length(fast)[0]:
                continue

            if previous_fast is not None:

                timedelta = fast.get("started") - previous_fast.get("stopped")

                if timedelta.total_seconds() <= seconds_per_day:

                    current_streak += 1

                else:

                    streaks.append(current_streak)
                    current_streak = 0

            previous_fast = fast

        if current_streak > 0:
            streaks.append(current_streak)

    return streaks


def __get_longest_fasting_streak(fasts: list) -> int:

    streaks = __get_fasting_streaks(fasts)

    return max(streaks) if len(streaks) > 0 else 0


def __get_current_fasting_streak(fasts: list) -> int:

    streaks = __get_fasting_streaks(fasts)

    return streaks[-1] if len(streaks) > 0 else 0


def __get_longest_fast_length(fasts: list) -> tuple:

    minutes_per_hour = 60
    max_minutes = 0

    for fast in fasts:

        hours, minutes = __get_fast_length(fast)
        minutes += hours * minutes_per_hour

        if minutes > max_minutes:
            max_minutes = minutes

    hours = max_minutes // minutes_per_hour
    minutes = max_minutes - hours * minutes_per_hour

    return hours, minutes


def __get_period_string(hours: float, minutes: float) -> str:

    return "{hours}h {minutes}m".format(hours=int(hours), minutes=int(minutes))
