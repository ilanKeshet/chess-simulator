from typing import Tuple


class Coordinate(object):
    def __init__(self, x: int, y: int):
        self.__validateRange('x', x)
        self.__validateRange('y', y)
        self._x: int = x
        self._y: int = y

    def getX(self) -> int:
        """Getter method for a Coordinate object's x coordinate (A.K.A: File)"""
        return self._x

    def getY(self) -> int:
        """Getter method for a Coordinate object's y coordinate (A.K.A: Rank)"""
        return self._y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return "Coordinate(%d, %d)" % (self._x, self._y)

    def moveOffset(self, offset: Tuple[int, int]) -> 'Coordinate':
        """offset tuple in the format (x, y)"""
        return Coordinate(self._x + int(offset[0]), self._y + int(offset[1]))

    @staticmethod
    def __validateRange(name: str, value: int) -> None:
        if value < 0 or value > 7:
            raise Exception("'" + name + "' value should be between 0 and 7, but was '" + value + "'")

    def __hash__(self) -> int:
        return hash(self._x) + (17 * hash(self._y))
