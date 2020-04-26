from typing import List

from src.board.Board import Board
from src.pieces.MovablePiece import MovablePiece
from src.board.Coordinate import Coordinate
from src.board.Color import Color
from src.pieces.PieceType import PieceType


class Pawn(MovablePiece):

    def __init__(self, position: Coordinate, color: Color):
        super().__init__(PieceType.PAWN, position, color)
        self._moveDirection: int = 1 if color == Color.WHITE else -1
        self._homeRowPosition: int = 1 if color == Color.WHITE else 6

    def getPossibleMoves(self, board: Board):
        moves: List[Coordinate] = []
        currPosition: Coordinate = self.getPosition()

        try:
            # single move forward
            newPosition = self.getPosition().moveOffset((0, self._moveDirection))
            if board.isVacant(newPosition):
                moves.append(newPosition)
                # double move forward from home position
                if currPosition.getY() == self._homeRowPosition:
                    newPosition = currPosition.moveOffset((0, 2 * self._moveDirection))
                    if board.isVacant(newPosition):
                        moves.append(newPosition)
        except Exception:
            # TODO raise Exception after Pawn promotion logic has been implemented
            pass

        for x in (1, -1):
            # eat left or right
            try:
                newPosition = currPosition.moveOffset((x, self._moveDirection))
                if board.canPieceAtPositionBeEaten(newPosition, self.getColor()):
                    moves.append(newPosition)
            except Exception:
                # pawn potential move had taken him to outside the board
                pass

        return moves