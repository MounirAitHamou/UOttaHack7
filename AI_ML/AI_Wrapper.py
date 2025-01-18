from Shared_Util.Piece import Piece
from Shared_Util.Gamestate import GameState
from AI import getBestMove


def getModelBestMove(gameState: GameState) -> Piece:
    bestMove: Piece = getBestMove()
    return bestMove


