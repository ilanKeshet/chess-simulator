from typing import Iterable, Tuple, List

from src.board.Board import Board
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType
from src.pieces.Piece import Piece


class MovablePiece(Piece):
    """movable chess piece interface"""

    _diagonals: Tuple[Tuple[int]] = ((1, 1), (-1, 1), (1, -1), (-1, -1))
    _cardinals: Tuple[Tuple[int]] = ((0, 1), (1, 0), (-1, 0), (0, -1))
    _galops: Tuple[Tuple[int]] = ((1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (1, -2), (-2, -1), (-1, -2))

    def __init__(self, pieceType: PieceType, position: Coordinate, color: Color):
        super().__init__(pieceType, position, color)

    def getPossibleMoves(self, board: Board):
        """get all the moves this piece can do"""
        raise Exception("base class can't actually move")
        pass

    def _generateMoves(self, board: Board, offsets: Iterable[Tuple[int]], maxPerOffset: int) -> List[Coordinate]:
        moves: List[Coordinate] = []
        for offset in offsets:
            currPosition: Coordinate = self.getPosition()
            insideBoard: bool = True
            canMoveAgainInDirection = True
            count: int = 0
            while insideBoard and canMoveAgainInDirection and maxPerOffset > count:
                count += 1

                try:
                    newPosition = currPosition.moveOffset(offset)
                    if board.isVacant(newPosition):
                        moves.append(newPosition)
                    else:
                        canMoveAgainInDirection = False
                        if board.canPieceAtPositionBeEaten(newPosition, self.getColor()):
                            moves.append(newPosition)
                except:
                    # ignoring illegal coordinates
                    insideBoard = False
                    pass
                currPosition = newPosition
        return moves

    def _getDiagnoals(self) -> Tuple[Tuple[int]]:
        return self._diagonals

    def _getCardinals(self) -> Tuple[Tuple[int]]:
        return self._cardinals

    def _getGalops(self) -> Tuple[Tuple[int]]:
        return self._galops
