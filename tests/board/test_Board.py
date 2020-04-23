from unittest import TestCase

from src.board.Board import Board
from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.simulator.Player import Player


class TestBoard(TestCase):

    def test_isVacant_positive_is_vacant(self):
        player1 = Player(Color.WHITE, [King(Coordinate(0, 0), Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(7, 7), Color.BLACK)])
        board = Board(player1.getPieces(), player2.getPieces())
        expected = True
        actual = board.isVacant(Coordinate(3, 3))
        self.assertEqual(expected, actual, "expected position to be vacant")

    def test_isVacant_positive_is_not_vacant(self):
        occupiedPosition = Coordinate(0, 6)
        player1 = Player(Color.WHITE, [King(occupiedPosition, Color.WHITE)])
        player2 = Player(Color.BLACK, [King(Coordinate(7, 7), Color.BLACK)])
        board = Board(player1.getPieces(), player2.getPieces())
        expected = False
        actual = board.isVacant(occupiedPosition)
        self.assertEqual(expected, actual, "expected position to be occupied")