from ..utils import *


def get_input(_func):
    """
    Custom function for USER input.
    Given a _func a custom message will be displayed for the USER.

    After USER selects one action function checks against all possible
    compinations. If USER input is in the approved actions the execution
    proceeds. While his registered action is not within the approved list USER
    is prompted to give an action again.

    :param _func: str
        Function which is called. This function name should me in both the
        console dict and the approved dict else KeyError is raised.
    :return: str
        User action after validation
    """

    console = {'action': " (1) Type One Tranformation\n"
                         " (2) Type Two Tranformation\n\n",
               'process': "\n(F)ast or (C)ustom processing ?\n\n"}

    approved = {'action': ['', '1', '2'],
                'process': ['F', 'C']}

    user_action = input(console[_func]).upper()
    accepted = ' or '.join(approved[_func])

    while user_action not in approved[_func]:
        display_error(f"Enter a valid input [{accepted}]\n")
        user_action = input(console[_func]).upper()

    return user_action
