from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Queen import Queen
from src.simulator.Player import Player
from tests.pieces.BaseMovementTest import BaseMovementTest


class TestQueen(BaseMovementTest):

    def test_queen_moves(self):
        queen = Queen(Coordinate(4, 4), Color.BLACK)
        player1 = Player(Color.BLACK, [queen, King(Coordinate(4, 5), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        expectedMoves = [Coordinate(5, 4), Coordinate(6, 4), Coordinate(7, 4), Coordinate(8, 4), Coordinate(9, 4),
                         Coordinate(10, 4), Coordinate(11, 4), Coordinate(12, 4), Coordinate(3, 4), Coordinate(2, 4),
                         Coordinate(1, 4), Coordinate(0, 4), Coordinate(-1, 4), Coordinate(-2, 4), Coordinate(-3, 4),
                         Coordinate(-4, 4), Coordinate(4, 3), Coordinate(4, 2), Coordinate(4, 1), Coordinate(4, 0),
                         Coordinate(4, -1), Coordinate(4, -2), Coordinate(4, -3), Coordinate(4, -4), Coordinate(5, 5),
                         Coordinate(6, 6), Coordinate(7, 7), Coordinate(8, 8), Coordinate(9, 9), Coordinate(10, 10),
                         Coordinate(11, 11), Coordinate(12, 12), Coordinate(3, 5), Coordinate(2, 6), Coordinate(1, 7),
                         Coordinate(0, 8), Coordinate(-1, 9), Coordinate(-2, 10), Coordinate(-3, 11),
                         Coordinate(-4, 12), Coordinate(5, 3), Coordinate(6, 2), Coordinate(7, 1), Coordinate(8, 0),
                         Coordinate(9, -1), Coordinate(10, -2), Coordinate(11, -3), Coordinate(12, -4),
                         Coordinate(3, 3), Coordinate(2, 2), Coordinate(1, 1), Coordinate(0, 0)]
        super()._testPieceMoves(queen, player1.getPieces(), player2.getPieces(), expectedMoves)
