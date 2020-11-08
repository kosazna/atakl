# -*- coding: utf-8 -*-

from aztool_akl.utilities.utils import *
from pathlib import Path


def validate_input(text: str) -> str:
    console = {'action': "(1) Concepts\n"
                         "(2) PT Beverages - Spirits\n"
                         "(3) PT Beverages - Lavazza\n\n"}

    approved = {'action': ['', '1', '2', '3']}

    action_mapper = {
        "1": "Concepts",
        "2": "PT Beverages - Spirits",
        "3": "PT Beverages - Lavazza"
    }

    user_action = input(console[text]).upper()
    accepted = 'Enter' + ' or '.join(approved[text])

    if user_action in approved[text]:
        return action_mapper[user_action]
    else:
        while user_action not in approved[text]:
            display_error(f"Enter a valid input [{accepted}]\n")
            user_action = input(console[text]).upper()

        return action_mapper[user_action]


def validate_path(text: str) -> (None, Path):
    user_path = input(text)

    if user_path == "":
        return None
    else:
        path = Path(user_path.strip('"'))

        if path.is_file():
            return path
        else:
            while not path.is_file():
                user_path = input("Path does not exist or is not valid")
                path = Path(user_path.strip('"'))

            return path


def validate_proper_and_existent_path(text: str):
    _path = Path(text).with_suffix('.xlsx')
    if not _path.parent.exists():
        _path.parent.mkdir()
    return Path(text).with_suffix('.xlsx')
