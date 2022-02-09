import random
import time

import constant
import strings
import user_queries
from controller import Controller
from modules.Board import Board


def fake_board_construct_message():
    print(strings.BUILDING_BOARD, end='')
    for i in range(random.randrange(2, 5)):
        time.sleep(0.5)
        print('.', end='')
    print()


if __name__ == '__main__':
    tower_names = list(constant.TOWERS_DICTIONARY.values())
    print(strings.WELCOME)
    time.sleep(1)
    print(strings.RULES.format(tower_names[-1]))
    time.sleep(2)
    # board = Board(2, tower_names)
    while True:
        rings_num = user_queries.query_rings_number()
        board = Board(rings_num, tower_names)
        fake_board_construct_message()
        controller = Controller(board)
        controller.game_loop()
        board.print_board()
        print("\n" + strings.GAME_WON)
        time.sleep(1)
        if not user_queries.query_yes_no("\n" + strings.REPLAY):
            break
