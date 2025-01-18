from Shared_Util.Piece import Piece
from ModelSingleton import ModelSingleton
import numpy as np
from Shared_Util.Gamestate import Gamestate
from Shared_Util.Pieces import Pieces




def processGamestate(gamestate: Gamestate):
    
    playfield = gamestate.playfield
    playfieldArray = np.array([[1 if pixel.Filled else 0 for pixel in row] for row in playfield])
    if gamestate:
        pass


def getBestMove() -> Piece:
    return Piece(0, 0, 0, 0)