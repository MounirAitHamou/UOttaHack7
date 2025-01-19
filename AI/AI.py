from Game.components.block import Block
from Game.components.grid import Grid

class AI:
    def __init__(self, candidate):
        self.heightWeight = candidate.heightWeight
        self.completeLinesWeight = candidate.completeLinesWeight
        self.holesWeight = candidate.holesWeight
        self.bumpinessWeight = candidate.bumpinessWeight

    def getMove(self, grid: Grid, block: Block):
        pass















































def getMoveParameters(grid: Grid, block: Block):
    moveParameters = []

    for rotationCount in range(4):
        for x in range(10):
            # If move is impossible, don't attempt it
            if not canMove(gameState, block):
                break

            # Copy the playfield to avoid modifying the original
            gameStateCopy: GameState = GameState()
            gameStateCopy.playfield = [[gameState.playfield[y][x] for x in range(10)] for y in range(20)]

            # Drop block as if it were played
            dropPiece(gameStateCopy, block)

            # Calculate the Aggregate Height
            aggregateHeight = 0
            for x in range(10):
                for y in range(20):
                    if gameStateCopy.playfield[y][x].filled:
                        aggregateHeight += 20 - y
                        break
            print("Aggregate height: " + str(aggregateHeight))

            # Calculate the Complete Lines
            totalCompleteLines: int = 0
            for y in range(20):
                lineComplete: bool = True
                for x in range(10):
                    if not gameStateCopy.playfield[y][x].filled:
                        lineComplete = False
                        break
                if lineComplete:
                    totalCompleteLines += 1
            print("Complete lines: " + str(totalCompleteLines))

            # Count number of holes
            totalHoles: int = 0
            for y in range(1, 20):
                for x in range(10):
                    if not gameStateCopy.playfield[y][x].filled:
                        isHole: bool = False
                        for y2 in range(y - 1, 0, -1):
                            if gameStateCopy.playfield[y2][x].filled:
                                isHole = True
                                break
                        if (isHole):
                            totalHoles += 1
            print("Total holes: " + str(totalHoles))

            # Calculate the Bumpiness
            bumpiness: int = 0
            previousColumnHeight: int
            for y in range(20):
                if gameStateCopy.playfield[y][0].filled:
                    previousColumnHeight = 20 - y
                    break
            for x in range(1, 10):
                for y in range(20):
                    if gameStateCopy.playfield[y][x].filled or y == 19:
                        bumpiness += abs(previousColumnHeight - (20 - y))
                        previousColumnHeight = 20 - y
                        break
            


            return MoveParameters(aggregateHeight, totalCompleteLines, totalHoles, bumpiness)


