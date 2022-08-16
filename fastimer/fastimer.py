#!/usr/bin/env python3

import keyboard
import datetime
import sys

from vkostyanetsky import cliutils

from fastimer import datafile, statistics, utils, browser
from fastimer.menu import FastimerMenu


def main() -> None:
    """
    Main entry point of the application. Displays the main menu by default.
    """

    main_menu()


def main_menu():

    fasts = datafile.read_fasts()
    active_fast = utils.get_active_fast(fasts)

    menu = FastimerMenu(active_fast)

    if active_fast is None:
        menu.add_item("Start New Fast", start_fast)
    else:
        menu.add_item("Stop Active Fast", stop_fast)

    menu.add_item("Fasts Browser", show_fasts_browser)
    menu.add_item("Statistics", show_statistics)
    menu.add_item("Exit", sys.exit)

    menu.choose()


def start_fast() -> None:
    fasts = datafile.read_fasts()
    fast = utils.get_active_fast(fasts)

    if fast is not None:

        print("Fast is already on.")
        print()

        cliutils.enter_to_continue()

    else:

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

                datafile.write_fasts(fasts)

            else:

                print("Please enter a valid number.")
                print()

                cliutils.enter_to_continue()

        main_menu()


def stop_fast() -> None:

    fasts = datafile.read_fasts()
    active_fast = utils.get_active_fast(fasts)

    menu = FastimerMenu(active_fast)

    menu.add_item("Finish Fast", finish_fast)
    menu.add_item("Cancel Fast", cancel_fast)
    menu.add_item("Back", main_menu)

    menu.choose()


def cancel_fast() -> None:
    """
    Cancel Fast
    """
    fasts = datafile.read_fasts()
    active_fast = utils.get_active_fast(fasts)

    cliutils.clear_terminal()

    prompt = "Do you want to CANCEL the active fast? It cannot be undone."

    if cliutils.prompt_for_yes_or_no(prompt):

        fasts.remove(active_fast)
        datafile.write_fasts(fasts)

    main_menu()


def finish_fast() -> None:
    """
    Finish Fast
    """
    fasts = datafile.read_fasts()

    cliutils.clear_terminal()

    if cliutils.prompt_for_yes_or_no("Do you want to end your ongoing fast?"):

        fasts[-1]["stopped"] = datetime.datetime.now()
        datafile.write_fasts(fasts)

    main_menu()


def show_fasts_browser() -> None:
    fasts = datafile.read_fasts()
    viewer = FastsBrowser(fasts)
    viewer.open()

    main_menu()


class FastsBrowser:

    _fasts: list = []
    _index: int = 0
    _max_index: int = 0

    def __init__(self, fasts: list):
        self._fasts = fasts

        self._max_index = len(fasts) - 1
        self._index = self._max_index

    def open(self) -> None:

        self.show_fast_by_index()

        print()
        print("Press [Left] and [Right] to switch fasts.")
        print("Press [Esc] to return to the main menu.")

        keyboard.add_hotkey('left', self.shift_left)
        keyboard.add_hotkey('right', self.shift_right)

        keyboard.wait('Esc')

    def show_fast_by_index(self):

        fasts = datafile.read_fasts()
        fast = fasts[self._index]

        fast_description = browser.get_fast_description(fast, include_zones=True)

        for line in fast_description:
            print(line)

    def shift_left(self):
        if self._index > 0:
            self._index -= 1
            self.show_fast_by_index()

    def shift_right(self):
        if self._index < self._max_index:
            self._index += 1
            self.show_fast_by_index()


def show_statistics() -> None:

    fasts = datafile.read_fasts()

    print("FASTING STATISTICS")
    print()

    statistics.print_completed_fasts(fasts)
    statistics.print_total_fasting_time(fasts)
    statistics.print_average_fast_length(fasts)
    statistics.print_longest_fast_length(fasts)
    statistics.print_longest_fasting_streak(fasts)
    statistics.print_current_fasting_streak(fasts)
    print()

    statistics.print_achievements(fasts)
    print()

    cliutils.enter_to_continue()

    main_menu()

x = 1