from itertools import chain
from typing import Iterable, List
from unittest import TestCase

from src.board.Board import Board
from src.board.Coordinate import Coordinate
from src.pieces.MovablePiece import MovablePiece
from src.pieces.Piece import Piece


class BaseMovementTest(TestCase):

    def _testPieceMoves(self, pieceUnderTest: MovablePiece, player1Pieces: Iterable[Piece], player2Pieces: Iterable[Piece], expectedMoves: List[Coordinate]):
        pieces = chain(player1Pieces, player2Pieces)
        board = Board(pieces)
        actualMoves = pieceUnderTest.getPossibleMoves(board)
        actualMoveDict = {}
        for am in actualMoves:
            actualMoveDict[am] = BaseMovementTest.MoveIndicator(am)

        expectedMoveDict = {}
        for em in expectedMoves:
            expectedMoveDict[em] = BaseMovementTest.MoveIndicator(em)

        print("actual moves")
        actualMoveDict[pieceUnderTest.getPosition()] = pieceUnderTest
        Board.printDict(actualMoveDict)

        print("expected moves")
        expectedMoveDict[pieceUnderTest.getPosition()] = pieceUnderTest
        Board.printDict(expectedMoveDict)

        self.assertEqual(actualMoves, expectedMoves, msg="expected and actual moves differ.")
        self.assertEqual(actualMoveDict, expectedMoveDict, msg="expected and actual moves dictionaries differ.")

    class MoveIndicator(Piece):
        def __init__(self, position: Coordinate):
            super().__init__(None, position, None)

        def __str__(self):
            return "*"

        def __eq__(self, other):
            return (
                    self.__class__ == other.__class__
                    and self.getPosition().__eq__(other.getPosition())
            )
