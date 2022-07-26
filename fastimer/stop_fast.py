#!/usr/bin/env python3

# noinspection PyPackageRequirements
import datetime

from consolemenu import PromptUtils

from .fasts_file import read_fasts, write_fasts
from .utils import get_active_fast


def stop_fast(prompt_utils: PromptUtils) -> None:

    fasts = read_fasts()
    fast = get_active_fast(fasts)

    if fast is not None:

        if prompt_utils.prompt_for_yes_or_no("Do you want to end your ongoing fast?"):

            fasts[-1]["stopped"] = datetime.datetime.now()
            write_fasts(fasts)

    else:

        print("No current fast to end.")
        print()

        prompt_utils.enter_to_continue()
