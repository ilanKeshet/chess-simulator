from src.board.Color import Color
from src.board.Move import Move
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
        gameBoard = GameBoard(self._player1, self._player2)
        playersByColor = {}
        playersByColor[self._player1.getColor()] = self._player1
        playersByColor[self._player2.getColor()] = self._player2
        if len(playersByColor) != 2:
            raise Exception("Could not determine color to player association")


        while True:
            for color in Color.getColorsByPrecedence():
                player = playersByColor[color]

                playerHasMadeValidMove: bool = False
                while not playerHasMadeValidMove:
                    move: Move = player.makeAMove(gameBoard.getBoard(), player)
                    if gameBoard.isValidMove(move, color):
                        gameBoard.move(move)
                        playerHasMadeValidMove = True
                        if gameBoard.isCheck(color):
                            print("player {} is in check".format(color.name))
                        # TODO
                        # # check for victory conditions
                        # victoriousColor: Color = gameBoard.findVictoriousColor()
                        # if victoriousColor is not None:
                        #     victoriousPlayer = playersByColor[victoriousColor]
                        #     # we have a winner...
                        #     return victoriousPlayer


