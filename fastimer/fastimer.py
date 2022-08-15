#!/usr/bin/env python3

import datetime
import sys

from vkostyanetsky import cliutils

from fastimer.menu import FastimerMainMenu
import fastimer.fasts_viewer
import fastimer.statistics
import fastimer.utils

from .fasts_file import read_fasts, write_fasts


def main() -> None:
    """
    Main entry point of the application. Displays the main menu by default.
    """

    main_menu()


def main_menu():

    fasts = read_fasts()
    active_fast = fastimer.utils.get_active_fast(fasts)

    menu = FastimerMainMenu(active_fast)

    if active_fast is None:
        menu.add_item("Start New Fast", start_fast)
    else:
        menu.add_item("Stop Active Fast", stop_fast)

    #menu.add_item("Fasts Browser", fasts_browser)
    menu.add_item("Statistics", statistics)
    menu.add_item("Exit", sys.exit)

    menu.choose()


def start_fast() -> None:
    fasts = read_fasts()
    fast = fastimer.utils.get_active_fast(fasts)

    if fast is not None:

        print("Fast is already on.")
        print()

        cliutils.enter_to_continue()

    else:

        fasts = read_fasts()

        length = None

        while length is None:

            user_input = input("Enter fast length: ")

            if user_input.isdigit():

                length = int(user_input)
                fast = {
                    "length": length,
                    "started": datetime.datetime.now(),
                }

                fasts.append(fast)
                write_fasts(fasts)

            else:

                print("Please enter a valid number.")
                print()

                cliutils.enter_to_continue()

        main_menu()


def stop_fast() -> None:

    menu = FastimerMainMenu()

    menu.add_item("Finish Fast", finish_fast)
    menu.add_item("Cancel Fast", cancel_fast)
    menu.add_item("Back", main_menu)

    menu.choose()


def cancel_fast() -> None:
    """
    Cancel Fast
    """
    fasts = read_fasts()
    active_fast = fastimer.utils.get_active_fast(fasts)

    cliutils.clear_terminal()

    prompt = "Do you want to CANCEL the active fast? It cannot be undone."

    if cliutils.prompt_for_yes_or_no(prompt):

        fasts.remove(active_fast)
        write_fasts(fasts)


def finish_fast() -> None:
    """
    Finish Fast
    """
    fasts = read_fasts()

    cliutils.clear_terminal()

    if cliutils.prompt_for_yes_or_no("Do you want to end your ongoing fast?"):

        fasts[-1]["stopped"] = datetime.datetime.now()
        write_fasts(fasts)


def fasts_browser() -> None:
    x = 1


def statistics() -> None:

    fasts = read_fasts()

    print("FASTING STATISTICS")
    print()

    fastimer.statistics.print_completed_fasts(fasts)
    fastimer.statistics.print_total_fasting_time(fasts)
    fastimer.statistics.print_average_fast_length(fasts)
    fastimer.statistics.print_longest_fast_length(fasts)
    fastimer.statistics.print_longest_fasting_streak(fasts)
    fastimer.statistics.print_current_fasting_streak(fasts)
    print()

    fastimer.statistics.print_achievements(fasts)
    print()

    cliutils.enter_to_continue()

    main_menu()
