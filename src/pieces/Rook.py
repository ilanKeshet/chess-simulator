from src.pieces.MovablePiece import MovablePiece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Rook(MovablePiece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.ROOK, position, color)

    def getPossibleMoves(self, board):
        directions = self._getCardinals()
        return self._generateMoves(board, directions, 8)