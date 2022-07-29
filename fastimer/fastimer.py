#!/usr/bin/env python3

# noinspection PyPackageRequirements
from consolemenu import ConsoleMenu, PromptUtils, Screen
# noinspection PyPackageRequirements
from consolemenu.items import FunctionItem as Item

from .cancel_fast import cancel_fast
from .fasts_file import read_fasts
from .show_fast import show_fast
from .show_statistics import show_statistics
from .start_fast import start_fast
from .stop_fast import stop_fast
from .utils import get_active_fast


def main() -> None:

    prompt = PromptUtils(Screen())
    params = [prompt]

    menu = ConsoleMenu("FASTING LOG")

    menu.append_item(Item("Start New Fast", start_fast, params))
    menu.append_item(Item("Manage Active Fast", manage_active_fast, params))
    menu.append_item(Item("Display Statistics", show_statistics, params))

    menu.show()


def manage_active_fast(prompt: PromptUtils) -> None:

    fasts = read_fasts()
    active_fast = get_active_fast(fasts)

    if active_fast is None:

        print("No current fast to manage.")
        print()

        prompt.enter_to_continue()

    else:

        params = [prompt, fasts, active_fast]

        menu = ConsoleMenu(
            title="ACTIVE FAST",
            subtitle="Choose the action you need:",
            exit_option_text="Back to Main Menu"
        )

        menu.append_item(Item("End Fast", stop_fast, params))
        menu.append_item(Item("Cancel Fast", cancel_fast, params))
        menu.append_item(Item("Display Fast", show_fast, params))

        menu.show()
