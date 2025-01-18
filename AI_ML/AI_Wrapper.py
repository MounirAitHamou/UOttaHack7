from Shared_Util.Piece import Piece
from Shared_Util.GameState import GameState
from AI_Shared.MoveParameters import MoveParameters
from Input_Processing.GameStateProcessor import moveParametersFromGameState
from Model.Model_Wrapper import evaluateMove

def getModelBestMove(gameState: GameState) -> Piece:
    moveParameters: list[MoveParameters] = moveParametersFromGameState(gameState)
    return evaluateMove(moveParameters)