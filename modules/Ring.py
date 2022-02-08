class Ring:
    def __init__(self, size: int):
        self._size = size

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    def visualize(self) -> str:
        return "*" + "**" * self.size

    def is_bigger(self, other) -> bool:
        return True if other is None else self.size > other.size

    @staticmethod
    def visualize_for_ring_size(ring_size: int):
        ring = Ring(ring_size)
        return ring.visualize()
