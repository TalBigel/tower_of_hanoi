from modules.Ring import Ring
from modules.Tower import Tower

BOARD_TOWER_LEVEL_FORMAT = "{0:{x}}\t{1:{x}}\t{2:{x}}"


class Board:
    def __init__(self, rings_num: int, tower_names: list[str]):
        self._tower_names = tower_names
        self._towers: list[Tower] = [Tower(name) for name in tower_names]
        self._max_ring: int = rings_num
        self._towers[0].add_rings([Ring(index) for index in range(rings_num, 0, -1)])

    @property
    def towers(self):
        return self._towers

    @property
    def tower_names(self):
        return self._tower_names

    @property
    def max_ring(self):
        return self._max_ring

    def get_tower_by_name(self, name: str) -> Tower:
        return next((tower for tower in self.towers if tower.name == name), None)

    def print_board(self):
        """
        Prints the towers of the game and the rings on them as *** representation
        """
        print()
        max_rings_in_tower = 0
        max_string_len = len(Ring.visualize_for_ring_size(self.max_ring))
        for tower in self.towers:
            max_rings_in_tower = max(max_rings_in_tower, len(tower.rings))

        for i in range(max_rings_in_tower - 1, -1, -1):
            level_string = []
            for tower in self.towers:
                ring = tower.get_ring_in_index(i)
                level_string.append((ring.visualize() if ring else "").center(max_string_len))

            print(BOARD_TOWER_LEVEL_FORMAT.format(level_string[0], level_string[1], level_string[2], x=max_string_len))

        level_string = []
        for tower in self.towers:
            level_string.append(tower.name.center(max_string_len))
        print(BOARD_TOWER_LEVEL_FORMAT.format(level_string[0], level_string[1], level_string[2], x=max_string_len))
