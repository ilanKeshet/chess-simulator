from random import choice, randrange
from typing import TypeVar, Iterable

from src.board.Board import Board
from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.board.Move import Move
from src.simulator import Player

P = TypeVar('P', bound='Piece')


class RandomMovingPlayer(Player):

    def __init__(self, color: Color = None, pieces: Iterable[P] = ()):
        super().__init__(color, pieces)

    def makeAMove(self, board: Board, color: Color) -> Move:
        """The only method a which needs to be implemented in order to extend a player and play the game
            please note that changing the board is meaningless and only the returned move is considered.

            :return: A Move object stating the Piece at which position should be move where
            :param board The layout of the board at the beginning of the turn
            :param color The Color of the piece the player should move in the current turn
        """

        while True:
            fromCoordinate = choice(list(board.getPieceDictionary().values())).getPosition()

            toCoordinate = Coordinate(randrange(0, 8), randrange(0, 8))
            if fromCoordinate != toCoordinate:
                return Move(fromCoordinate, toCoordinate)
