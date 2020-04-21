from src.pieces.Piece import Piece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Queen(Piece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.QUEEN, position, color)

