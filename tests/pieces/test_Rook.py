from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Rook import Rook
from src.simulator.Player import Player
from tests.pieces.BaseMovementTest import BaseMovementTest


class TestRook(BaseMovementTest):

    def test_rook_moves(self):
        rook = Rook(Coordinate(4, 4), Color.BLACK)
        player1 = Player(Color.BLACK, [rook, King(Coordinate(4, 5), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        expectedMoves = [Coordinate(5, 4), Coordinate(6, 4), Coordinate(7, 4), Coordinate(8, 4), Coordinate(9, 4),
                         Coordinate(10, 4), Coordinate(11, 4), Coordinate(12, 4), Coordinate(3, 4), Coordinate(2, 4),
                         Coordinate(1, 4), Coordinate(0, 4), Coordinate(-1, 4), Coordinate(-2, 4), Coordinate(-3, 4),
                         Coordinate(-4, 4), Coordinate(4, 3), Coordinate(4, 2), Coordinate(4, 1), Coordinate(4, 0),
                         Coordinate(4, -1), Coordinate(4, -2), Coordinate(4, -3), Coordinate(4, -4)]
        super()._testPieceMoves(rook, player1.getPieces(), player2.getPieces(), expectedMoves)
