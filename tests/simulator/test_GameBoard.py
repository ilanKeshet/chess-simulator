from unittest import TestCase

from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.PieceType import PieceType
from src.pieces.Queen import Queen
from src.simulator.GameBoard import GameBoard
from src.simulator.Player import Player


class TestGameBoard(TestCase):

    def test_isVacant_positive_is_vacant(self):
        player1 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(7, 7), Color.BLACK)])
        board = GameBoard(player1, player2)
        expected = True
        actual = board.isVacant(Coordinate(3, 3))
        self.assertEqual(expected, actual, "expected position to be vacant")

    def test_isVacant_positive_is_not_vacant(self):
        occupiedPosition = Coordinate(0, 6)
        player1 = Player(Color.WHITE, [King(occupiedPosition, Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(7, 7), Color.BLACK)])
        board = GameBoard(player1, player2)
        expected = False
        actual = board.isVacant(occupiedPosition)
        self.assertEqual(expected, actual, "expected position to be occupied")

    def test_isKing_positive(self):
        king = King(Coordinate(0, 0), Color.BLACK)
        expected = True
        actual = GameBoard.isKing(king)
        self.assertEqual(expected, actual, msg="king wasn't properly identified")

    def test_isKing_negative(self):
        queen = Queen(Coordinate(0, 0), Color.BLACK)
        expected = False
        actual = GameBoard.isKing(queen)
        self.assertEqual(expected, actual, msg="queen was misidentified as a king")

    def test_findKing_positive(self):
        expected = King(Coordinate(1,1), Color.WHITE)
        pieces = [expected]
        actual = GameBoard.findKing(pieces)
        self.assertEqual(expected, actual, "unable to find king")

    def test_findKing_negative_no_king(self):
        pieces = [Knight(Coordinate(1, 1), Color.WHITE)]
        self.assertRaises(Exception, GameBoard.findKing, pieces)

    def test_findKing_negative_too_many_kings(self):
        pieces = [King(Coordinate(1, 1), Color.WHITE), King(Coordinate(1, 2), Color.WHITE)]
        self.assertRaises(Exception, GameBoard.findKing, pieces)

    def test_player_default_pieces_has_a_king(self):
        for color in Color:
            pieces = GameBoard.generateDefaultPiecePlacement(color)
            king = GameBoard.findKing(pieces)
            self.assertEqual(color, king.getColor(), "king's color differs from requested color set")
            self.assertEqual(PieceType.KING, king.getPieceType(), "received king isn't a king at all")

    def test_default_piece_placement(self):
        expectedPieceCount = 16
        for color in Color:
            player1 = Player(color)
            player2 = Player(Color.getOpositeColor(color))

            GameBoard.generateDefaultPiecePlacementIfBothPlayersHaveNoPieces(player1, player2)
            self.assertEqual(expectedPieceCount, len(player1.getPieces()), "unexpected piece count create for player1")
            self.assertEqual(expectedPieceCount, len(player2.getPieces()), "unexpected piece count create for player2")
