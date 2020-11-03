# -*- coding: utf-8 -*-

from aztool_akl.utils import *
from pathlib import Path


def validate_input(text: str) -> str:
    console = {'action': "(1) Concepts\n"
                         "(2) PT Beverages - Spirits\n"
                         "(3) PT Beverages - Lavazza\n\n",
               'process': "\n(F)ast or (C)ustom processing ?\n\n"}

    approved = {'action': ['', '1', '2', '3'],
                'process': ['F', 'C']}

    user_action = input(console[text]).upper()
    accepted = ' or '.join(approved[text])

    if user_action in approved[text]:
        return user_action
    else:
        while user_action not in approved[text]:
            display_error(f"Enter a valid input [{accepted}]\n")
            user_action = input(console[text]).upper()

        return user_action


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
