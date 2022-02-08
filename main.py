import random
import time

from modules.Board import Board
from modules.Ring import Ring
from modules.Tower import Tower

TOWERS_FORMAT = "{0:{x}}\t{1:{x}}\t{2:{x}}"


def print_board(game_state):
    for i in range(0, 3):
        print(TOWERS_FORMAT.format(game_state["a"][i], game_state["b"][i], game_state["c"][i], x=4))
    print(TOWERS_FORMAT.format("a", "b", "c", x=4))


def query_rings_number() -> int:
    num = None
    while True:
        try:
            num = int(input("Enter the number of rings you'd like to play with: "))
            if num < 2:
                raise ValueError
            break
        except ValueError:
            print("Please input an integer larger than 1...")
            continue

    return num


def fake_board_construct_message():
    print("Building board, please wait", end='')
    for i in range(random.randrange(2, 5)):
        time.sleep(0.5)
        print('.', end='')
    print()


if __name__ == '__main__':
    tower_names = ["a", "b", "c"]
    print("Welcome to Towers of Hanoi!")
    # time.sleep(1)
    print("In order to win, you need to move all the rings to the tower {}.".format(tower_names[-1]))
    print("You can only move a ring to a tower that has no rings, "
          "or that its top ring is larger than the one you're moving")
    # time.sleep(2)
    rings_num = query_rings_number()
    # board = Board(rings_num, tower_names)
    board = Board(2, tower_names)
    # fake_board_construct_message()
    board.print_board()



    game_state = {"a": [3, 2, 1], "b": [0, 0, 0], "c": [0, 0, 0]}
    while True:
        print_board(game_state)
        source = input("Choose source: ")
        print(source)
        target = input("Choose target: ")
        print(target)
        if source not in game_state or target not in game_state:
            print("Invalid values. Can only use 'a', 'b' and 'c'")
            continue
        if source == target:
            print("Can't choose the same source and target")
            continue

        rings_source = game_state.get(source)
        rings_target = game_state.get(target)
        max_source = max(rings_source)
        max_target = max(rings_target)
        if max_source < max_target:
            print("The target tower has a bigger ring than the source tower")
            continue

        rings_source[rings_source.index(max_source)] = 0
        rings_target[max([i for i, x in enumerate(rings_target) if x == 0])] = max_source

        if list(range(3, 0, -1)) == game_state.get("c"):
            break

    print("You won!")
