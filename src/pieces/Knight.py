from src.pieces.MovablePiece import MovablePiece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Knight(MovablePiece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.KNIGHT, position, color)

    def getPossibleMoves(self, board):
        directions = self._getGalops()
        return self._generateMoves(board, directions, 1)