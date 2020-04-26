from src.board.Board import Board
from src.pieces.MovablePiece import MovablePiece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Bishop(MovablePiece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.BISHOP, position, color)

    def getPossibleMoves(self, board: Board):
        directions = self._getDiagnoals()
        return self._generateMoves(board, directions, 8)