from Game.components.block import Block
from Game.components.grid import Grid
from Game.Trainer import Trainer
from AI.GameComponentUtils import cloneBlock, cloneGrid, lockBlock, attemptToMoveLeft, attemptToMoveRight, moveDown, checkValid
from AI.MoveParameters import MoveParameters
import copy

class AI:
    def __init__(self, candidate):
        self.heightWeight = candidate["heightWeight"]
        self.completeLinesWeight = candidate["linesWeight"]
        self.holesWeight = candidate["holesWeight"]
        self.bumpinessWeight = candidate["bumpinessWeight"]

    def best(self, grid:Grid, playingPieces, playingPieceIndex = 0):
        best = None
        bestScore = None
        playingPiece = playingPieces[playingPieceIndex]


        for rotation in range(4):
            piece = cloneBlock(playingPiece)

            for _ in range(rotation):
                piece.rotate()
            attemptToMoveLeft(grid, piece)
            
            
            while(checkValid(grid, piece)):
                pieceCopy = cloneBlock(piece)
                moveDown(grid, pieceCopy)
                gridClone = cloneGrid(grid)
                lockBlock(gridClone,pieceCopy)
                score = None
                moveParameters = getMoveParameters(gridClone)
                if playingPieceIndex == (len(playingPieces) - 1):
                    score = -self.heightWeight * moveParameters.AggregateHeight + self.completeLinesWeight * moveParameters.CompleteLines - self.holesWeight * moveParameters.Holes - self.bumpinessWeight * moveParameters.Bumpiness
                else:
                    score = self.best(gridClone, playingPieces, playingPieceIndex + 1)[1]
                if bestScore == None or score>bestScore:
                    bestScore = score
                    best = cloneBlock(pieceCopy)
                attemptToMoveRight(grid, piece)
        return (best, bestScore)




def getMoveParameters(grid: Grid):
    aggregateHeight = 0
    for x in range(10):
        for y in range(20):
            if grid.grid[y][x] > 0:
                aggregateHeight += 20 - y
                break

    totalCompleteLines: int = 0
    for y in range(20):
        lineComplete: bool = True
        for x in range(10):
            if not grid.grid[y][x] > 0:
                lineComplete = False
                break
        if lineComplete:
            totalCompleteLines += 1
    
    totalHoles: int = 0
    for y in range(1, 20):
        for x in range(10):
            if not grid.grid[y][x] > 0:
                isHole: bool = False
                for y2 in range(y - 1, 0, -1):
                    if grid.grid[y2][x] > 0:
                        isHole = True
                        break
                if (isHole):
                    totalHoles += 1

    bumpiness: int = 0
    previousColumnHeight: int = 0
    for y in range(20):
        if grid.grid[y][0] > 0 or y == 19:
            previousColumnHeight = 20 - y
            break
    for x in range(1, 10):
        for y in range(20):
            if grid.grid[y][x] > 0 or y == 19:
                bumpiness += abs(previousColumnHeight - (20 - y))
                previousColumnHeight = 20 - y
                break
    return MoveParameters(aggregateHeight, totalCompleteLines, totalHoles, bumpiness)


