from modules.Board import Board
from modules.Ring import Ring
from modules.Tower import Tower

TOWERS_FORMAT = "{0:{x}}\t{1:{x}}\t{2:{x}}"


def print_board(game_state):
    for i in range(0, 3):
        print(TOWERS_FORMAT.format(game_state["a"][i], game_state["b"][i], game_state["c"][i], x=4))
    print(TOWERS_FORMAT.format("a", "b", "c", x=4))


if __name__ == '__main__':
    board = Board(5, ["a", "b", "c"])
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
