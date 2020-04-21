from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Piece(object):
    """basic chess piece interface"""

    def __init__(self, pieceType: PieceType, position: Coordinate, color: Color):
        """
        :type pieceType: PieceType
        :type position: Coordinate
        :type color: Color
        """
        self._pieceType: PieceType = pieceType
        self._position: Coordinate = position
        self._color: Color = color

    def getPosition(self) -> Coordinate:
        """coordinate on the board"""
        return self._position

    def getPieceType(self) -> PieceType:
        return self._pieceType

    def getColor(self) -> Color:
        return self._color

    def __str__(self):
        pieceLetter = str(self._pieceType.value)
        if self._color == Color.BLACK:
            return pieceLetter
        elif self._color == Color.WHITE:
            return str(pieceLetter.upper())
        else:
            raise Exception("invalid color {}".format(self._color))

    def __repr__(self):
        """Returns representation of the object"""
        return "{}({!r})".format(self.__class__.__name__, self._pieceType, self._position, self._color)
