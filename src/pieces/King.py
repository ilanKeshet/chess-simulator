from src.pieces.MovablePiece import MovablePiece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class King(MovablePiece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.KING, position, color)

    def getPossibleMoves(self, board):
        directions = self._getCardinals() + self._getDiagnoals()
        potentialMoves = self._generateMoves(board, directions, 1)
        # TODO filter moves leading in to a Check position out of potentialMoves
        # TODO add Castling moves
        return potentialMoves
