from modules.Ring import Ring


class Tower:

    def __init__(self, name: str):
        self._name = name
        self._rings: list[Ring] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def rings(self) -> list[Ring]:
        return self._rings

    def pop(self) -> Ring:
        return self.rings.pop()

    def top(self) -> Ring:
        if len(self.rings) > 0:
            return self.rings[-1]

    def get_ring_in_index(self, index) -> Ring:
        if 0 <= index < len(self.rings):
            return self.rings[index]

    def add_ring(self, ring: Ring):
        self.rings.append(ring)

    def add_rings(self, rings: list[Ring]):
        self.rings.extend(rings)

    def get_rings_amount(self) -> int:
        return len(self.rings)
