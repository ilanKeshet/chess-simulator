from typing import List, TypeVar, Iterable

from src.board.Board import Board
from src.board.Color import Color
from src.board.Move import Move

P = TypeVar('P', bound='Piece')


class Player:

    def __init__(self, color: Color = None, pieces: Iterable[P] = ()):
        self._color: Color = color
        self._pieces: List[P] = list(pieces)

    def getColor(self) -> Color:
        return self._color

    def setColor(self, color: Color) -> None:
        self._color = color

    def getPieces(self) -> List[P]:
        return self._pieces

    def setPieces(self, pieces: Iterable[P]) -> None:
        self._pieces = list(pieces)

    def makeAMove(self, board: Board, color: Color) -> Move:
        """The only method a which needs to be implemented in order to extend a player and play the game
            please note that changing the board is meaningless and only the returned move is considered.

            :return: A Move object stating the Piece at which position should be move where
            :param board The layout of the board at the beginning of the turn
            :param color The Color of the piece the player should move in the current turn
        """
        pass
