from itertools import chain
from unittest import TestCase

from src.board.Board import Board
from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.King import King
from src.pieces.Queen import Queen


class TestBoard(TestCase):

    def test_all_and_only_pieces_are_being_set_on_the_board(self):
        player1Pieces = [King(Coordinate(0, 0), Color.WHITE)]
        player2Pieces = [King(Coordinate(7, 7), Color.BLACK)]
        pieces = list(chain(player1Pieces, player2Pieces))
        board = Board(pieces)
        boardPieceDictionary = board._getPieceDictionary()
        self.assertEqual(len(pieces), len(boardPieceDictionary), msg="Expected amount of pieces to match")
        for expectedPiece in pieces:
            actualPiece = boardPieceDictionary.get(expectedPiece.getPosition(), None)
            self.assertEqual(expectedPiece, actualPiece, "Missing or unexpected piece on the board")

    def test_overlapping_pieces_from_different_colors_cause_an_error(self):
        player1Pieces = [King(Coordinate(0, 0), Color.WHITE)]
        player2Pieces = [King(Coordinate(0, 0), Color.BLACK)]
        pieces = chain(player1Pieces, player2Pieces)
        self.assertRaises(Exception, Board, pieces)

    def test_overlapping_pieces_from_same_color_cause_an_error(self):
        player1Pieces = [King(Coordinate(0, 0), Color.WHITE), Queen(Coordinate(0, 0), Color.WHITE)]
        player2Pieces = [King(Coordinate(7, 7), Color.BLACK)]
        pieces = chain(player1Pieces, player2Pieces)
        self.assertRaises(Exception, Board, pieces)

    def test_isVacant_positive_is_vacant(self):
        player1Pieces = [King(Coordinate(0, 0), Color.WHITE)]
        player2Pieces = [King(Coordinate(7, 7), Color.BLACK)]
        board = Board(chain(player1Pieces, player2Pieces))
        expected = True
        actual = board.isVacant(Coordinate(3, 3))
        self.assertEqual(expected, actual, "expected position to be vacant")

    def test_isVacant_positive_is_not_vacant(self):
        occupiedPosition = Coordinate(0, 6)
        player1Pieces = [King(occupiedPosition, Color.WHITE)]
        player2Pieces = [King(Coordinate(7, 7), Color.BLACK)]
        board = Board(chain(player1Pieces, player2Pieces))
        expected = False
        actual = board.isVacant(occupiedPosition)
        self.assertEqual(expected, actual, "expected position to be occupied")