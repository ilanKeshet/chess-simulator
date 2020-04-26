from src.board.Board import Board
from src.pieces.MovablePiece import MovablePiece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Queen(MovablePiece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.QUEEN, position, color)

    def getPossibleMoves(self, board: Board):
        directions = self._getCardinals() + self._getDiagnoals()
        return self._generateMoves(board, directions, 8)