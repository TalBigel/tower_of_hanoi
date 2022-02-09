import random
import time

import constant
import strings
from modules.Board import Board
from modules.Tower import Tower


def query_rings_number() -> int:
    num = None
    while True:
        try:
            num = int(input(strings.RINGS_NUMBER_QUERY))
            if num < 2:
                raise ValueError
            break
        except ValueError:
            print(strings.RINGS_NUMBER_ERROR)
            continue

    return num


def fake_board_construct_message():
    print(strings.BUILDING_BOARD, end='')
    for i in range(random.randrange(2, 5)):
        time.sleep(0.5)
        print('.', end='')
    print()


def query_tower(board: Board, query_str: str) -> Tower:
    while True:
        tower_name = input(query_str)
        tower = board.get_tower_by_name(tower_name)
        if tower is not None:
            return tower
        else:
            print(strings.INVALID_TOWER_ERROR)


if __name__ == '__main__':
    tower_names = list(constant.TOWERS_DICTIONARY.values())
    print(strings.WELCOME)
    # time.sleep(1)
    print(strings.RULES.format(tower_names[-1]))
    # time.sleep(2)
    rings_num = query_rings_number()
    board = Board(rings_num, tower_names)
    # board = Board(2, tower_names)
    # fake_board_construct_message()
    while True:
        board.print_board()
        source = query_tower(board, strings.SELECT_SOURCE_TOWER.format(*tower_names))
        target = query_tower(board, strings.SELECT_TARGET_TOWER.format(*tower_names))
        source_top = source.top()
        target_top = target.top()

        if source_top is None:
            print(strings.SOURCE_TOWER_NO_RINGS_ERROR.format(source.name))
            continue

        if target_top is not None and source_top.is_bigger(target_top):
            print(strings.INVALID_MOVE_ERROR.
                  format(target.name, source.name))
            continue

        ring = source.pop()
        target.add_ring(ring)

        if board.get_tower_by_name(constant.TOWERS_DICTIONARY.get("goal")).get_rings_amount() == board.max_ring:
            break

    board.print_board()
    print()
    print(strings.GAME_WON)
