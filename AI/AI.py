from Game.components.block import Block
from Game.components.grid import Grid
from Game.Trainer import Trainer
from GameComponentUtils import cloneBlock, cloneGrid, lockBlock
from MoveParameters import MoveParameters
import copy

class AI:
    def __init__(self, candidate):
        self.heightWeight = candidate["heightWeight"]
        self.completeLinesWeight = candidate["completeLinesWeight"]
        self.holesWeight = candidate["holesWeight"]
        self.bumpinessWeight = candidate["bumpinessWeight"]

    def best(self, trainer:Trainer, playingPieces):
        dupeTrainer = copy.deepcopy(trainer)
        playingPieceIndex = 0
        best = None
        bestScore = None
        playingPiece = playingPieces[playingPieceIndex]


        for rotation in range(4):
            piece = cloneBlock(playingPiece)
            for _ in range(rotation):
                piece.rotate()
            dupeTrainer.attemptToMoveLeft(piece)
            
            
            while(dupeTrainer.checkValid(piece)):
                pieceCopy = cloneBlock(piece)
                dupetrainer.moveDown(pieceCopy)
                gridClone = cloneGrid(trainer.game.grid)
                lockBlock(pieceCopy, gridClone)
                score = None
                moveParameters = getMoveParameters(gridClone)
                if playingPieceIndex == (len(playingPieces) - 1):
                    score = -self.heightWeight * moveParameters.AggregateHeight + self.completeLinesWeight * moveParameters.CompleteLines - self.holesWeight * moveParameters.Holes - self.bumpinessWeight * moveParameters.Bumpiness
                else:
                    score = self.best(dupeTrainer, playingPieces[playingPieceIndex + 1])
                if score>bestScore or bestScore == None:
                    bestScore = score
                    best = cloneBlock(pieceCopy)
                dupeTrainer.moveRight(piece)




def getMoveParameters(grid: Grid):
    aggregateHeight = 0
    for x in range(10):
        for y in range(20):
            if grid[y][x].filled:
                aggregateHeight += 20 - y
                break

    totalCompleteLines: int = 0
    for y in range(20):
        lineComplete: bool = True
        for x in range(10):
            if not grid[y][x].filled:
                lineComplete = False
                break
        if lineComplete:
            totalCompleteLines += 1
    
    totalHoles: int = 0
    for y in range(1, 20):
        for x in range(10):
            if not grid[y][x].filled:
                isHole: bool = False
                for y2 in range(y - 1, 0, -1):
                    if grid[y2][x].filled:
                        isHole = True
                        break
                if (isHole):
                    totalHoles += 1

    bumpiness: int = 0
    previousColumnHeight: int
    for y in range(20):
        if grid[y][0].filled:
            previousColumnHeight = 20 - y
            break
    for x in range(1, 10):
        for y in range(20):
            if grid[y][x].filled or y == 19:
                bumpiness += abs(previousColumnHeight - (20 - y))
                previousColumnHeight = 20 - y
                break
    return MoveParameters(aggregateHeight, totalCompleteLines, totalHoles, bumpiness)


