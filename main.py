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


def query_tower(board: Board, query_str: str) -> Tower:
    while True:
        tower_name = input(query_str)
        tower = board.get_tower_by_name(tower_name)
        if tower is not None:
            return tower
        else:
            print("Invalid tower. Can only select")


if __name__ == '__main__':
    tower_names = ["a", "b", "c"]
    print("Welcome to Towers of Hanoi!")
    # time.sleep(1)
    print("In order to win, you need to move all the rings to the tower {}.".format(tower_names[-1]))
    print("You can only move a ring to a tower that has no rings, "
          "or that its top ring is larger than the one you're moving")
    # time.sleep(2)
    rings_num = query_rings_number()
    board = Board(rings_num, tower_names)
    # board = Board(2, tower_names)
    # fake_board_construct_message()
    while True:
        board.print_board()
        source = query_tower(board, "Please select source tower from {}, {} or {}: ".format(*tower_names))
        target = query_tower(board, "Please select target tower from {}, {} or {}: ".format(*tower_names))
        source_top = source.top()
        target_top = target.top()

        if source_top is None:
            print("The source tower {} has no rings!".format(source.name))
            continue

        if target_top is not None and source_top.is_bigger(target_top):
            print("The target tower {} top ring is smaller than the source tower {} top ring!".
                  format(target.name, source.name))
            continue

        ring = source.pop()
        target.add_ring(ring)

        if board.get_tower_by_name("c").get_rings_amount() == board.max_ring:
            break

    board.print_board()
    print()
    print("You won!")

