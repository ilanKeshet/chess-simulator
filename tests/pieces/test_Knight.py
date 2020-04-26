from copy import deepcopy

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

    def test_cloning(self):
        original = Knight(Coordinate(6, 5), Color.WHITE)
        originalPieces = [original]
        copiedPieces = deepcopy(originalPieces)
        a_copy = copiedPieces[0]

        self.assertNotEqual(originalPieces, copiedPieces, "Expected collection to differ")
        self.assertFalse(original == a_copy, "Expected collection references to differ")
        self.assertEqual(original.getColor(), a_copy.getColor(), "Expected colors to equal")
        self.assertTrue(original.getColor() == a_copy.getColor(), "Expected colors to be equal '=='")
        self.assertTrue(original.getColor() is a_copy.getColor(), "Expected colors to reference same Enum")
        self.assertEqual(original.getPieceType(), a_copy.getPieceType(), "Expected pieceTypes to equal")
        self.assertTrue(original.getPieceType() == a_copy.getPieceType(), "Expected pieceTypes to be equal '=='")
        self.assertTrue(original.getPieceType() is a_copy.getPieceType(), "Expected pieceTypes to reference same Enum")
        self.assertEqual(original.getPosition(), a_copy.getPosition(), "Expected positions to equal")
        self.assertTrue(original.getPosition() == a_copy.getPosition(), "Expected positions to be equal '=='")
        self.assertFalse(original.getPosition() is a_copy.getPosition(), "Expected positions to not be the same object")
