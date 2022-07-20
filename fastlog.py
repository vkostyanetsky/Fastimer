import datetime
import sys
from collections import namedtuple
from os.path import join

from consolemenu import ConsoleMenu, PromptUtils, Screen
from consolemenu.items import FunctionItem
from consolemenu.validators.regex import RegexValidator
from yaml import parser, safe_dump, safe_load


def main() -> None:
    data = namedtuple("data", "path journal")

    data.path = sys.argv[1] if len(sys.argv) > 1 else ""

    read_journal(data)
    display_menu(data)


def get_journal_file_name() -> str:
    return "journal.yaml"


def read_journal(data: namedtuple):
    yaml_file_path = join(data.path, get_journal_file_name())

    try:

        with open(yaml_file_path, encoding="utf-8-sig") as yaml_file:
            data.journal = safe_load(yaml_file)

            if data.journal is None:
                data.journal = []

    except FileNotFoundError:

        print(f"File is not found: {yaml_file_path}")
        sys.exit(1)

    except parser.ParserError:

        print(f"Unable to parse: {yaml_file_path}")
        sys.exit(1)


def write_journal(data: namedtuple):
    yaml_file_path = join(data.path, get_journal_file_name())

    with open(yaml_file_path, encoding="utf-8-sig", mode="w") as yaml_file:
        safe_dump(data.journal, yaml_file)


def display_menu(data: namedtuple):
    """
    Builds and then displays main menu of the application.
    """

    prompt_utils = PromptUtils(Screen())
    items_params = [data, prompt_utils]

    menu = ConsoleMenu("FASTING LOG")

    menu.append_item(FunctionItem("Display Fast", display_fast, items_params))
    menu.append_item(FunctionItem("Start Fast", start_fast, items_params))
    menu.append_item(FunctionItem("End Fast", end_fast, items_params))

    menu.show()


def display_fast(data: namedtuple, prompt_utils: PromptUtils):
    fast = get_current_fast(data)

    if fast is None:
        print("No current fast to display.")
    else:
        goal = fast["started"] + datetime.timedelta(hours=fast["length"])

        elapsed_time = get_elapsed_time(fast)
        remaining_time = get_time(datetime.datetime.today(), goal)

        started = fast["started"].strftime("%a, %H:%M")

        goal = goal.strftime("%a, %H:%M")

        print(f'CURRENT FAST:    {fast["length"]} HOURS')
        print()
        print(f"Elapsed time:    {elapsed_time}")
        print(f"Remaining:       {remaining_time}")
        print()
        print(f"Started:  {started}")
        print(f"Goal:     {goal}")

    print()
    prompt_utils.enter_to_continue()


def start_fast(data: namedtuple, prompt_utils: PromptUtils):
    fast = get_current_fast(data)

    if fast is not None:

        print("Fast is already on.")
        prompt_utils.enter_to_continue()

    else:

        length = None
        length_validator = RegexValidator("^[0-9]*$")

        while length is None:
            input_result = prompt_utils.input(
                prompt="Enter fast length: ", default="16", validators=length_validator
            )
            if input_result.validation_result:
                length = int(input_result.input_string)
                fast = {
                    "length": length,
                    "started": datetime.datetime.now(),
                    "stopped": None,
                }

                data.journal.append(fast)
                write_journal(data)
            else:
                print("Please enter a valid number.")


def end_fast(data: namedtuple, prompt_utils: PromptUtils):
    fast = get_current_fast(data)

    if fast is not None:

        if prompt_utils.prompt_for_yes_or_no("Do you want to end your ongoing fast? "):

            data.journal[-1]["stopped"] = datetime.datetime.now()
            write_journal(data)

    else:

        print("No current fast to end.")
        print()

        prompt_utils.enter_to_continue()


def get_time(start_date: datetime, end_date: datetime) -> str:
    seconds = (end_date - start_date).total_seconds()
    hours = int(seconds / 60 / 60)
    minutes = int((seconds - hours * 60 * 60) / 60)
    seconds = int(seconds - hours * 60 * 60 - minutes * 60)

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    return f"{hours}:{minutes}:{seconds}"


def get_elapsed_time(fast: dict) -> str:
    date1 = fast["started"]
    date2 = datetime.datetime.today() if fast["stopped"] is None else fast["stopped"]

    return get_time(date1, date2)


def get_current_fast(data: namedtuple):
    return (
        data.journal[-1]
        if len(data.journal) > 0 and data.journal[-1]["stopped"] is None
        else None
    )


if __name__ == "__main__":
    main()
