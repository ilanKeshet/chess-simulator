from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.simulator.Player import Player
from tests.pieces.BaseMovementTest import BaseMovementTest


class TestKnight(BaseMovementTest):

    def test_knight_moves(self):
        knight = Knight(Coordinate(4, 4), Color.BLACK)
        player1 = Player(Color.BLACK, [knight, King(Coordinate(6, 3), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        expectedMoves = [Coordinate(5, 6), Coordinate(6, 5), Coordinate(3, 6), Coordinate(2, 5),
                         Coordinate(5, 2), Coordinate(2, 3), Coordinate(3, 2)]
        super()._testPieceMoves(knight, player1.getPieces(), player2.getPieces(), expectedMoves)
