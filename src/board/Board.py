from typing import Dict, TypeVar
from itertools import chain
from src.board.Coordinate import Coordinate
from src.simulator.Player import Player
from src.pieces.Piece import Piece

P = TypeVar('P', bound='Piece')
C = TypeVar('C', bound='Coordinate')


class Board(object):

    def __init__(self, player1: Player, player2: Player):
        self.board: Dict[C, P] = {}
        for piece in chain(player1.getPieces(), player2.getPieces()):
            prev: Piece = self.board.get(piece.getPosition())
            if prev is not None:
                raise Exception(
                    "piece placement conflict, for position '{}'. existing value: '{}' new value: '{}'."
                    .format(piece.getPosition(), prev, piece))
            self.board[piece.getPosition()] = piece
        self.printBoard()

    def printBoard(self) -> None:
        print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
        for y in range(7, -1, -1):
            print("-" * 35)
            print(chr(y + 97) + " " , end="| ")
            for x in range(0, 8, 1):
                coordinate = Coordinate(x, y)
                item = self.board.get(coordinate, " ")
                print(str(item) + ' |', end=" ")
            print()
        print("-" * 35)
        print("")

    def isVacant(self, position: Coordinate) -> bool:
        return self.board.get(position, None) is None
