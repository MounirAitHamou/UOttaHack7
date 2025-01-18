from Pixel import Pixel
from Pieces import Pieces
from Piece import Piece

class Gamestate:
    def __init__(self,
                 playfield: list[list[Pixel]] = [[Pixel() for _ in range(20)] for _ in range(10)],
                 holdPiece: Pieces = None,
                 nextPieces: list[Pieces] = [Piece.generateRandomPiece() for _ in range(3)],
                 score: int = 0,
                 bestMove: Piece = None):
        self.playfield = playfield
        self.holdPiece = holdPiece
        self.nextPieces = nextPieces
        self.score = score
        self.bestMove = bestMove
