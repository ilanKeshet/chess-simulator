from enum import Enum, unique


@unique
class PieceType(Enum):
    PAWN = "p"
    ROOK = "r"
    BISHOP = "b"
    KNIGHT = "h"
    KING = "k"
    QUEEN = "q"
