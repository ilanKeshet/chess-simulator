from typing import Dict, TypeVar, Iterable

from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.Piece import Piece

P = TypeVar('P', bound='Piece')
C = TypeVar('C', bound='Coordinate')


class Board(object):

    def __init__(self, pieces: Iterable[P]):
        self._pieceDictionary: Dict[C, P] = {}
        for piece in pieces:
            prev: Piece = self._pieceDictionary.get(piece.getPosition())
            if prev is not None:
                raise Exception(
                    "piece placement conflict, for position '{}'. existing value: '{}' new value: '{}'."
                    .format(piece.getPosition(), prev, piece))
            self._pieceDictionary[piece.getPosition()] = piece
        self.printBoard()

    def _getPieceDictionary(self) -> Dict[C, P]:
        return self._pieceDictionary

    def printBoard(self) -> None:
        Board.printDict(self._pieceDictionary)

    @staticmethod
    def printDict(dict) -> None:
        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for y in range(7, -1, -1):
            print("-" * 35)
            print(chr(y + 97) + " " , end="| ")
            for x in range(0, 8, 1):
                coordinate = Coordinate(x, y)
                item = dict.get(coordinate, " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 35)
        print("")

    def isVacant(self, position: Coordinate) -> bool:
        return self._getPieceDictionary().get(position, None) is None

    def canPieceAtPositionBeEaten(self, position: Coordinate, color: Color) -> bool:
        return not self.isVacant(position) and self._getPieceDictionary().get(position).getColor() != color
