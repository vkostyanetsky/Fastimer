#!/usr/bin/env python3

import datetime

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .fasts_file import write_fasts


def stop_fast(prompt: PromptUtils, fasts: list, fast: dict) -> None:

    if prompt.prompt_for_yes_or_no("Do you want to end your ongoing fast?"):

        fasts[-1]["stopped"] = datetime.datetime.now()
        write_fasts(fasts)
