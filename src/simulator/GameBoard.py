from copy import deepcopy
from typing import TypeVar, Iterable, List
from itertools import chain

from src.board.Board import Board
from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.pieces.Bishop import Bishop
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.Pawn import Pawn
from src.pieces.PieceType import PieceType
from src.pieces.Queen import Queen
from src.pieces.Rook import Rook
from src.pieces.Piece import Piece
from src.simulator import Player

P = TypeVar('P', bound='Piece')
C = TypeVar('C', bound='Coordinate')


class GameBoard(Board):

    def __init__(self, player1: Player, player2: Player):
        """
        Note that Player objects are only used to initialize the board's piece positions
        The passed in Player object may be mutated if:
           - Any of the player's didn't yet have color assigned
           - Both players do not have pieces, at which case a default piece placement is generated
        """
        GameBoard.validatePlayerColorChoicesAndAssignColorsIfNeeded(player1, player2)
        GameBoard.generateDefaultPiecePlacementIfBothPlayersHaveNoPieces(player1, player2)
        GameBoard.validatePlayerPieces(player1)
        GameBoard.validatePlayerPieces(player2)

        # note we defensibly copy all pieces so no one else would have a reference to them
        super().__init__(deepcopy(chain(player1.getPieces(), player2.getPieces())))


    def getBoard(self) -> Board:
        clonedPieces = deepcopy(self._getPieceDictionary().values())
        return Board(clonedPieces)

    @staticmethod
    def generateDefaultPiecePlacementIfBothPlayersHaveNoPieces(player1: Player, player2: Player) -> None:
        if len(player1.getPieces()) == 0 and len(player2.getPieces()) == 0:
            player1.setPieces(GameBoard.generateDefaultPiecePlacement(player1.getColor()))
            player2.setPieces(GameBoard.generateDefaultPiecePlacement(player2.getColor()))

    @staticmethod
    def validatePlayerPieces(player: Player) -> None:
        pieces: List[P] = player.getPieces()
        GameBoard.validateAllPiecesMatchColor(pieces, player.getColor())

        if len(pieces) > 16:
            raise Exception("Player has too many pieces: {}".format(pieces))
        if len(pieces) < 1:
            raise Exception("Player doesn't have enough pieces: {}".format(pieces))

        GameBoard.findKing(pieces)
        # Theoretically we can check more things but it gets complicated due to Pawn promotion, so enough for now

    @staticmethod
    def validatePlayerColorChoicesAndAssignColorsIfNeeded(player1: Player, player2: Player) -> None:
        if player1.getColor() is None and player2.getColor() is None:
            p1Color: Color = Color.getRandomColor()
            player1.setColor(p1Color)
            player2.setColor(Color.getOpositeColor(p1Color))
        elif player1.getColor() is None:
            player2.setColor(Color.getOpositeColor(player1.getColor()))
        elif player2.getColor() is None:
            player1.setColor(Color.getOpositeColor(player2.getColor()))
        elif player1.getColor() == player2.getColor():
            raise Exception("both players have same color")

    @staticmethod
    def findKing(pieces: List[P]) -> King:
        res = list(filter(GameBoard.isKing, pieces))
        if len(res) == 1:
            return res[0]
        elif len(res) > 1:
            raise Exception("Too many kings {}".format(res))
        else:
            raise Exception("No King found")

    @staticmethod
    def isKing(piece: Piece) -> King:
        return piece.getPieceType() == PieceType.KING

    @staticmethod
    def generateDefaultPiecePlacement(color: Color) -> List[P]:
        pieces = GameBoard.generateDefaultPawnRow(color)
        pieces.extend(GameBoard.generateDefaultRoyaltyRow(color))
        return pieces

    @staticmethod
    def generateDefaultRoyaltyRow(color: Color) -> List[P]:
        baseRow: int = 0 if color == Color.WHITE else 7

        pieces: List[P] = [
            Rook(Coordinate(0, baseRow), color),
            Knight(Coordinate(1, baseRow), color),
            Bishop(Coordinate(2, baseRow), color),
            Queen(Coordinate(3, baseRow), color),
            King(Coordinate(4, baseRow), color),
            Bishop(Coordinate(5, baseRow), color),
            Knight(Coordinate(6, baseRow), color),
            Rook(Coordinate(7, baseRow), color)
        ]
        return pieces

    @staticmethod
    def generateDefaultPawnRow(color: Color) -> List[P]:
        baseRow: int = 1 if color == Color.WHITE else 6

        pieces: List[P] = []
        for i in range(8):
            position = Coordinate(int(i), baseRow)
            pawn = Pawn(position, color)
            pieces.append(pawn)

        return pieces

    @staticmethod
    def validateAllPiecesMatchColor(pieces: Iterable[P], color: Color) -> None:
        pp: Piece
        for pp in pieces:
            if color != pp.getColor():
                raise Exception("Color mismatch detected: expected '{}' but was '{}'".format(color, pp.getColor()))
