from src.board.Coordinate import Coordinate


class Move(object):

    def __init__(self, fromPosition: Coordinate, toPosition: Coordinate):
        if fromPosition is None or toPosition is None:
            raise Exception("move positions may not be None")
        if fromPosition == toPosition:
            raise Exception("'from' and 'to' positions may not be the same coordinate")
        self._fromPosition = fromPosition
        self._toPosition = toPosition

    def getFromPosition(self) -> Coordinate:
        return self._fromPosition

    def getToPosition(self) -> Coordinate:
        return self._toPosition