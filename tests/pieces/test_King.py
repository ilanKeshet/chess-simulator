from copy import deepcopy

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

    def test_cloning(self):
        original = King(Coordinate(6, 5), Color.WHITE)
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
