from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Pawn import Pawn
from src.simulator.Player import Player
from tests.pieces.BaseMovementTest import BaseMovementTest


class TestPawn(BaseMovementTest):

    def test_black_pawn_single_move_forward(self):
        pawn = Pawn(Coordinate(4, 4), Color.BLACK)
        player1 = Player(Color.BLACK, [pawn, King(Coordinate(4, 6), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        expectedMoves = [Coordinate(4, 3)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_black_pawn_single_move_forward_leap_obstructed(self):
        pawn = Pawn(Coordinate(1, 6), Color.BLACK)
        player1 = Player(Color.BLACK, [pawn, King(Coordinate(1, 4), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        expectedMoves = [Coordinate(1, 5)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_black_pawn_single_move_forward_and_leap_forward_and_left_right_eating(self):
        pawn = Pawn(Coordinate(1, 6), Color.BLACK)
        player1 = Player(Color.BLACK, [pawn, King(Coordinate(1, 3), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE),
                                       Pawn(Coordinate(0, 5), Color.WHITE),
                                       Pawn(Coordinate(2, 5), Color.WHITE)])
        expectedMoves = [Coordinate(1, 5), Coordinate(1, 4), Coordinate(2, 5), Coordinate(0, 5)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_black_pawn_single_eat_right_and_left_obstructed(self):
        pawn = Pawn(Coordinate(1, 4), Color.BLACK)
        player1 = Player(Color.BLACK, [pawn, King(Coordinate(1, 5), Color.BLACK),
                                       Pawn(Coordinate(0, 3), Color.BLACK),
                                       Pawn(Coordinate(2, 3), Color.BLACK)])
        player2 = Player(Color.WHITE, [King(Coordinate(0, 1), Color.WHITE)])
        expectedMoves = [Coordinate(1, 3)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_white_pawn_single_move_forward(self):
        pawn = Pawn(Coordinate(4, 4), Color.WHITE)
        player1 = Player(Color.WHITE, [pawn, King(Coordinate(4, 6), Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(0, 0), Color.BLACK)])
        expectedMoves = [Coordinate(4, 5)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_white_pawn_single_move_forward_leap_obstructed(self):
        pawn = Pawn(Coordinate(1, 1), Color.WHITE)
        player1 = Player(Color.WHITE, [pawn, King(Coordinate(1, 3), Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(0, 0), Color.BLACK)])
        expectedMoves = [Coordinate(1, 2)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_white_pawn_single_move_forward_and_leap_forward_and_left_right_eating(self):
        pawn = Pawn(Coordinate(1, 1), Color.WHITE)
        player1 = Player(Color.WHITE, [pawn, King(Coordinate(1, 4), Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(0, 0), Color.BLACK),
                                       Pawn(Coordinate(0, 2), Color.BLACK),
                                       Pawn(Coordinate(2, 2), Color.BLACK)])
        expectedMoves = [Coordinate(1, 2), Coordinate(1, 3), Coordinate(2, 2), Coordinate(0, 2)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)

    def test_white_pawn_single_eat_right_and_left_obstructed(self):
        pawn = Pawn(Coordinate(1, 2), Color.WHITE)
        player1 = Player(Color.BLACK, [pawn, King(Coordinate(1, 5), Color.WHITE),
                                       Pawn(Coordinate(0, 3), Color.WHITE),
                                       Pawn(Coordinate(2, 3), Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(0, 1), Color.BLACK)])
        expectedMoves = [Coordinate(1, 3)]
        super()._testPieceMoves(pawn, player1.getPieces(), player2.getPieces(), expectedMoves)
