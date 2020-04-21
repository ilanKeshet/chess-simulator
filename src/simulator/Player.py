from typing import List, TypeVar

from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.Bishop import Bishop
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.Pawn import Pawn
from src.pieces.Queen import Queen
from src.pieces.Rook import Rook

P = TypeVar('P', bound='Piece')


class Player:
    _pieces: List[P] = []
    color: Color = None

    def __init__(self, color: Color, pieces: List[P]=[]):
        self.color = color
        if len(pieces) == 0:
            self._pieces = self.generateDefaultPiecePlacment()
        else:
            # TODO validate pieces
            self._pieces = pieces


    def getPieces(self) -> List[P]:
        return self._pieces

    def getColor(self) -> Color:
        return self.color

    def generateDefaultPiecePlacment(self) -> List[P]:
        pieces = self.generateDefaultPawnRow(self.color)
        pieces.extend(self.generateDefaultRoyaltyRow(self.color))
        return pieces

    @staticmethod
    def generateDefaultRoyaltyRow(color: Color) -> List[P]:
        baseRow: int = 0 if color == Color.WHITE else 7

        pieces: List[P] = [
            Rook(Coordinate(0, baseRow), color),
            Knight(Coordinate(1, baseRow), color),
            Bishop(Coordinate(2, baseRow), color),
            Queen(Coordinate(3, baseRow), color),
            King(Coordinate(4, baseRow), color),
            Bishop(Coordinate(5, baseRow), color),
            Knight(Coordinate(6, baseRow), color),
            Rook(Coordinate(7, baseRow), color)
        ]
        return pieces

    @staticmethod
    def generateDefaultPawnRow(color: Color) -> List[P]:
        baseRow: int = 1 if color == Color.WHITE else 6

        pieces: List[P] = []
        for i in range(8):
            position = Coordinate(int(i), baseRow)
            pawn = Pawn(position, color)
            pieces.append(pawn)

        return pieces
