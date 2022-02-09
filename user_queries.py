import sys

import constant
import strings
from modules.Board import Board
from modules.Tower import Tower


def query_tower(board: Board, query_str: str) -> Tower:
    while True:
        tower_name = input(query_str)
        tower = board.get_tower_by_name(tower_name)
        if tower is not None:
            return tower
        else:
            print(strings.INVALID_TOWER_ERROR)


def query_rings_number() -> int:
    num = None
    while True:
        try:
            num = int(input(strings.RINGS_NUMBER_QUERY))
            if num < constant.MIN_NUMBER_RINGS:
                raise ValueError
            break
        except ValueError:
            print(strings.RINGS_NUMBER_ERROR)
            continue

    return num


def query_yes_no(question, default="yes") -> bool:
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
