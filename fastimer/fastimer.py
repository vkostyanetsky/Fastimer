#!/usr/bin/env python3

# noinspection PyPackageRequirements
from consolemenu import ConsoleMenu, PromptUtils, Screen

# noinspection PyPackageRequirements
from consolemenu.items import FunctionItem

from .show_fast import show_fast
from .show_statistics import show_statistics
from .start_fast import start_fast
from .stop_fast import stop_fast


def main() -> None:
    """
    Builds and then displays main menu of the application.
    """

    prompt = PromptUtils(Screen())
    params = [prompt]

    menu = ConsoleMenu("FASTING LOG")

    menu.append_item(FunctionItem("Start New Fast", start_fast, params))
    menu.append_item(FunctionItem("End Active Fast", stop_fast, params))
    menu.append_item(FunctionItem("Display Active Fast", show_fast, params))
    menu.append_item(
        FunctionItem("Display Fasting Statistics", show_statistics, params)
    )

    menu.show()
