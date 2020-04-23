from typing import Dict, TypeVar, Iterable
from itertools import chain

from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.Piece import Piece

P = TypeVar('P', bound='Piece')
C = TypeVar('C', bound='Coordinate')


class Board(object):

    def __init__(self, player1Pieces: Iterable[P], player2Pieces: Iterable[P]):
        self.board: Dict[C, P] = {}
        for piece in chain(player1Pieces, player2Pieces):
            prev: Piece = self.board.get(piece.getPosition())
            if prev is not None:
                raise Exception(
                    "piece placement conflict, for position '{}'. existing value: '{}' new value: '{}'."
                    .format(piece.getPosition(), prev, piece))
            self.board[piece.getPosition()] = piece
        self.printBoard()

    def printBoard(self) -> None:
        Board.printDict(self.board)

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
        return self.board.get(position, None) is None

    def canPieceAtPositionBeEaten(self, position: Coordinate, color: Color) -> bool:
        return not self.isVacant(position) and self.board.get(position).getColor() != color
