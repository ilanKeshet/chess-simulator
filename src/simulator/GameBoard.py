from builtins import Exception
from copy import deepcopy
from typing import TypeVar, Iterable, List, Dict
from itertools import chain

from src.board.Board import Board
from src.board.Color import Color
from src.board.Coordinate import Coordinate
from src.board.Move import Move
from src.pieces.Bishop import Bishop
from src.pieces.King import King
from src.pieces.Knight import Knight
from src.pieces.MovablePiece import MovablePiece
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
        super().__init__(deepcopy(chain(player1.getPieces(), player2.getPieces())), printBoard=True)
        self._moveCount: int = 0

    def getBoard(self) -> Board:
        clonedPieces = deepcopy(list(self.getPieceDictionary().values()))
        return Board(clonedPieces)

    def isValidMove(self, move: Move, color: Color) -> bool:
        try:
            _move = Move(move.getFromPosition(), move.getToPosition())
        except:
            # we somehow got a bad Move object, perhaps a sub class...
            return False

        pieceDictionary: Dict[C, P] = super().getPieceDictionary()
        pieceAtFromPosition: Piece = pieceDictionary.get(_move.getFromPosition())
        if pieceAtFromPosition is None:
            # Nothing to move there
            return False
        elif pieceAtFromPosition.getColor() != color:
            # Tried to move piece of the wrong color
            return False

        if not GameBoard.__canPieceMoveToRequestedPosition(self.getBoard(), pieceAtFromPosition, _move.getToPosition()):
            return False

        # will move result in check
        boardAfterMove: Board = self.getBoard().simulateMove(move)
        if GameBoard.isInCheck(boardAfterMove, color):
            # we are in check and the move does not resolve the check
            return False

        # we couldn't find anything wrong with the move with the currently implemented logic
        return True

    def move(self, move: Move) -> None:
        pieceDictionary: Dict[Coordinate, Piece] = self.getPieceDictionary()
        piece = pieceDictionary[move.getFromPosition()]
        del pieceDictionary[move.getFromPosition()]
        newPiece: MovablePiece = GameBoard.pieceFactory(piece.getPieceType(), move.getToPosition(), piece.getColor())
        eatenPiece = pieceDictionary.get(move.getToPosition(), None)
        pieceDictionary[move.getToPosition()] = newPiece

        print("")
        print("Board print number {}".format(self._moveCount))
        self.printBoard()
        if eatenPiece is not None:
            print("the {} {} was eaten".format(eatenPiece.getColor().name, eatenPiece.getPieceType().name))

            # TODO this exit shouldn't be here
            if eatenPiece.getPieceType() == PieceType.KING:
                print("the {} player has lost".format(eatenPiece.getColor().name))
                exit()

        self._moveCount += 1

    @staticmethod
    def pieceFactory(pieceType: PieceType, position: Coordinate, color: Color) -> MovablePiece:
        # TODO replace this ugly thing with method producing a new MovablePiece of same type from each movable piece
        if pieceType == PieceType.PAWN:
            return Pawn(position, color)
        elif pieceType == PieceType.KING:
            return King(position, color)
        elif pieceType == PieceType.QUEEN:
            return Queen(position, color)
        elif pieceType == PieceType.ROOK:
            return Pawn(position, color)
        elif pieceType == PieceType.BISHOP:
            return Bishop(position, color)
        elif pieceType == PieceType.KNIGHT:
            return Knight(position, color)
        else:
            raise Exception("Unable to instantiate piece of type '{}'".format(pieceType))

    def isCheck(self, color: Color) -> bool:
        return GameBoard.isInCheck(self.getBoard(), color)

    @staticmethod
    def isInCheck(board: Board, color: Color) -> bool:
        king = GameBoard.findKingOfColor(board, color)
        opposingPieces: List[Piece] = GameBoard.findAllPiecesOfColor(board, Color.getOpositeColor(color))
        for opposingPiece in opposingPieces:
            if GameBoard.__canPieceMoveToRequestedPosition(board, opposingPiece, king.getPosition()):
                return True
        return False

    @staticmethod
    def findKingOfColor(board: Board, color: Color) -> King:
        piecesOfColor: List[Piece] = GameBoard.findAllPiecesOfColor(board, color)
        return GameBoard.findKing(piecesOfColor)

    @staticmethod
    def findAllPiecesOfColor(board: Board, color: Color) -> List[Piece]:
        return filter(lambda piece: GameBoard.isPieceColor(piece, color), board.getPieceDictionary().values())

    @staticmethod
    def __canPieceMoveToRequestedPosition(board:Board, piece: Piece, toPosition: Coordinate):
        if not isinstance(piece, MovablePiece):
            raise Exception("Encountered non MovablePiece instance in GameBoard: '{}'".format(piece))
        # Cast to MovablePiece
        movablePiece: MovablePiece = piece
        possibleMoves = movablePiece.getPossibleMoves(board)
        if toPosition in possibleMoves:
            return True
        else:
            # piece at from position can't make a the move to requested position
            return False

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
    def isPieceColor(piece: Piece, color: Color) -> bool:
        return color == piece.getColor()

    @staticmethod
    def isKing(piece: Piece) -> bool:
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
