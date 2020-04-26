from src.simulator.GameBoard import GameBoard
from src.simulator.Player import Player


class Simulator:
    def __init__(self, player1: Player, player2: Player):
        self._player1: Player = player1
        self._player2: Player = player2

    def run(self):
        """
        This method actually invokes the players logic, and return the winner
        """
        board = GameBoard(self._player1, self._player2)
        while True:
            for player in (self._player1, self._player2):
                pass
            return None