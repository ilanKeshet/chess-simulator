from typing import List, TypeVar

from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.Bishop import Bishop
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.Pawn import Pawn
from src.pieces.PieceType import PieceType
from src.pieces.Queen import Queen
from src.pieces.Rook import Rook
from src.pieces.Piece import Piece

P = TypeVar('P', bound='Piece')


class Player:

    def __init__(self, color: Color, pieces: List[P]=[]):
        self._color: Color = color
        if len(pieces) == 0:
            self._pieces: List[P] = self.generateDefaultPiecePlacment(color)
        else:
            # TODO consider adding more logic validating player pieces
            self._king: King = Player.findKing(pieces)
            if len(pieces) > 16:
                raise Exception("Player has too many pieces: {}".format(pieces))
            self._pieces: List[P] = pieces

    @staticmethod
    def findKing(pieces: List[P]) -> King:
        res = list(filter(Player.isKing, pieces))
        if len(res) == 1:
            return res[0]
        elif len(res) > 1:
            raise Exception("Too many kings {}".format(res))
        else:
            raise Exception("No King found")

    @staticmethod
    def isKing(piece: Piece) -> King:
        return piece.getPieceType() == PieceType.KING

    def getPieces(self) -> List[P]:
        return self._pieces

    def getColor(self) -> Color:
        return self._color

    def getKing(self) -> King:
        return self._king

    @staticmethod
    def generateDefaultPiecePlacment(color: Color) -> List[P]:
        pieces = Player.generateDefaultPawnRow(color)
        pieces.extend(Player.generateDefaultRoyaltyRow(color))
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