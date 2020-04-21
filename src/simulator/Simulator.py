from src.board.Board import Board
from src.simulator.Player import Player


class Simulator:
    def __init__(self, player1: Player, player2: Player):
        self._player1: Player = player1
        self._player2: Player = player2

    def run(self):
        """
        This method actually invokes the players logic, and return the winner
        """
        board = Board(self._player1.getPieces(), self._player2.getPieces())
