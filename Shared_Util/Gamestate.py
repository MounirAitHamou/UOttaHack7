from Shared_Util.Pixel import Pixel
from Shared_Util.Pieces import Pieces
from Shared_Util.Piece import Piece

class GameState:
    def __init__(self,
                 playfield: list[list[Pixel]] = [[Pixel() for _ in range(20)] for _ in range(10)],
                 holdPiece: Pieces = None,
                 nextPieces: list[Pieces] = [Piece.generateRandomPiece() for _ in range(3)],
                 score: int = 0,
                 bestMove: Piece = None,
                 tickTime: int = 1,
                 playerPiece: Piece = None,
                 ):
        self.playfield = playfield
        self.holdPiece = holdPiece
        self.nextPieces = nextPieces
        self.score = score
        self.bestMove = bestMove
        self.tickTime = tickTime
        self.playerPiece = playerPiece

    def display(self):
        for row in self.playfield:
            for pixel in row:
                print(1 if pixel.filled else 0, end='')
            print()
       
