from Shared_Util.GameState import GameState
from AI_ML.AI_Shared.MoveParameters import MoveParameters

def moveParametersFromGameState(gameState: GameState) -> MoveParameters:
    for rotationCount in range(4):
        for x in range(10):
            if canMove(gameState, x, rotationCount):
                # Step 1: Clean up the playfield
                cleanedPlayfield = [[gameState.playfield[x][y].filled for y in range(20)] for x in range(10)]
                print(cleanedPlayfield)

                # Step 2: Calculate the Aggregate Height
                aggregateHeight = 0
                for x in range(10):
                    for y in range(20):
                        if cleanedPlayfield[x][y]:
                            aggregateHeight += 20 - y
                            break
                print("Aggregate height: " + aggregateHeight)

def canMove(gameState, x, rotationCount):
    return True