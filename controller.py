import constant
import strings
import user_queries
from modules.Board import Board


class Controller:
    """
    A class that holds the main logic of the game.
    """
    def __init__(self, board: Board):
        self._board = board

    @property
    def board(self) -> Board:
        return self._board

    def _is_game_won(self) -> bool:
        """
        Checks whether the game is won. The game is won if all the rings are on the last tower

        :return:
            whether the game is won or not
        """
        goal_tower_name = constant.TOWERS_DICTIONARY.get("goal")
        return self.board.get_tower_by_name(goal_tower_name).get_rings_amount() == self.board.max_ring

    def game_loop(self):
        """The main game loop of the game where the user moves rings from tower to tower.

        The loop ends when the game is won.
        """
        board = self.board
        tower_names = board.tower_names
        while True:
            board.print_board()
            source = user_queries.query_tower(board, strings.SELECT_SOURCE_TOWER.format(*tower_names))
            target = user_queries.query_tower(board, strings.SELECT_TARGET_TOWER.format(*tower_names))
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

            if self._is_game_won():
                break
