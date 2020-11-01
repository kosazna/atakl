from ..utils import *
from pathlib import Path


def validate_input(text: str) -> str:
    console = {'action': " (1) Type One Tranformation\n"
                         " (2) Type Two Tranformation\n\n",
               'process': "\n(F)ast or (C)ustom processing ?\n\n"}

    approved = {'action': ['', '1', '2'],
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


def validate_path(text: str) -> Path:
    user_path = input(text)
    path = Path(user_path.strip('"'))

    if path.is_file():
        return path
    else:
        while not path.is_file():
            user_path = input("Path does not exist or is not valid")
            path = Path(user_path.strip('"'))

        return path
