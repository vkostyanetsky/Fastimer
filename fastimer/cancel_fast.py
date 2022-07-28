#!/usr/bin/env python3

import datetime

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .fasts_file import read_fasts, write_fasts
from .utils import get_active_fast


def cancel_fast(prompt: PromptUtils) -> None:

    fasts = read_fasts()
    fast = get_active_fast(fasts)

    if fast is not None:

        if prompt.prompt_for_yes_or_no("Do you want to CANCEL your ongoing fast? It cannot be undone."):

            fasts.remove(fast)
            write_fasts(fasts)

    else:

        print("No current fast to cancel.")
        print()

        prompt.enter_to_continue()
