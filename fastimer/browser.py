#!/usr/bin/env python3

import keyboard
from vkostyanetsky import cliutils

from fastimer import view


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

        keyboard.add_hotkey("left", self.shift_left)
        keyboard.add_hotkey("right", self.shift_right)

        keyboard.wait("Esc")

    def show_fast_by_index(self):

        cliutils.clear_terminal()

        fast = self._fasts[self._index]

        fast_description = view.get(fast, include_zones=True)

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
