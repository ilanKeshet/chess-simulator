from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.simulator.Player import Player
from tests.pieces.BaseMovementTest import BaseMovementTest


class TestKing(BaseMovementTest):

    def test_king_moves(self):
        king = King(Coordinate(4,4), Color.BLACK)
        player1 = Player(Color.BLACK, [king, Knight(Coordinate(4,5), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        expectedMoves = [Coordinate(5, 4), Coordinate(3, 4), Coordinate(4, 3), Coordinate(5, 5),
                         Coordinate(3, 5), Coordinate(5, 3), Coordinate(3, 3)]
        super()._testPieceMoves(king, player1.getPieces(), player2.getPieces(), expectedMoves)
