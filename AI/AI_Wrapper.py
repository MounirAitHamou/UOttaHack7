import AI.AI as AI

def getBestMove(grid,playingPieces):
    weights = {
        "heightWeight": 0.510066,
        "linesWeight": 0.760666,
        "holesWeight": 0.35663,
        "bumpinessWeight": 0.184483
    }
    ai = AI.AI(weights)
    return ai.best(grid,playingPieces)[0]
