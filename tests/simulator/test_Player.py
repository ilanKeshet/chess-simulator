from unittest import TestCase

from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.Knight import Knight
from src.pieces.PieceType import PieceType
from src.pieces.Queen import Queen
from src.simulator.Player import Player
from src.pieces.King import King


class TestPlayer(TestCase):

    def test_isKing_positive(self):
        king = King(Coordinate(0, 0), Color.BLACK)
        expected = True
        actual = Player.isKing(king)
        self.assertEqual(expected, actual, msg="king wasn't properly identified")

    def test_isKing_negative(self):
        queen = Queen(Coordinate(0, 0), Color.BLACK)
        expected = False
        actual = Player.isKing(queen)
        self.assertEqual(expected, actual, msg="queen was misidentified as a king")

    def test_findKing_positive(self):
        expected = King(Coordinate(1,1), Color.WHITE)
        pieces = [expected]
        actual = Player.findKing(pieces)
        self.assertEqual(expected, actual, "unable to find king")

    def test_findKing_negative_no_king(self):
        pieces = [Knight(Coordinate(1, 1), Color.WHITE)]
        self.assertRaises(Exception, Player.findKing, pieces)

    def test_findKing_negative_too_many_kings(self):
        pieces = [King(Coordinate(1, 1), Color.WHITE), King(Coordinate(1, 2), Color.WHITE)]
        self.assertRaises(Exception, Player.findKing, pieces)

    def test_player_default_pieces_has_a_king(self):
        for color in Color:
            pieces = Player.generateDefaultPiecePlacment(color)
            king = Player.findKing(pieces)
            self.assertEqual(color, king.getColor(), "king's color differs from requested color set")
            self.assertEqual(PieceType.KING, king.getPieceType(), "received king isn't a king at all")

    def test_player_default_constructor(self):
        expectedPieceCount = 16
        for color in Color:
            player = Player(color)
            self.assertEqual(expectedPieceCount, len(player.getPieces()), "unexpected piece count create for player")