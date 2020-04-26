from unittest import TestCase

from src.board.Color import Color
from src.simulator.Player import Player


class TestPlayer(TestCase):
    def test_player_created_without_pieces_has_no_pieces(self):
        expectedPieceCount = 0
        for color in Color:
            player1 = Player(color)
            player2 = Player(Color.getOpositeColor(color))
            self.assertEqual(expectedPieceCount, len(player1.getPieces()), "expected player created without pieces to have no pieces")
            self.assertEqual(expectedPieceCount, len(player2.getPieces()), "expected player created without pieces to have no pieces")

    def test_player_created_without_color_has_no_color(self):
        player1 = Player()
        self.assertIsNone(player1.getColor(), "expected player created without a color to have no Color")
