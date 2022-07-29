#!/usr/bin/env python3

# noinspection PyPackageRequirements
from consolemenu import PromptUtils

from .fasts_file import write_fasts


def cancel_fast(prompt: PromptUtils, fasts: list, active_fast: dict) -> None:

    question = "Do you want to CANCEL the active fast? It cannot be undone."

    if prompt.prompt_for_yes_or_no(question):

        fasts.remove(active_fast)
        write_fasts(fasts)
