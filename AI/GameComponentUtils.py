import copy
from Game.components.block import Block
from Game.components.grid import Grid

def cloneBlock(block: Block) -> Block:
    return copy.deepcopy(block)

def lockBlock(grid: Grid, block: Block):
    tiles = block.get_cell_positions()
    for position in tiles:
        grid.grid[position.row][position.column] = block.id

def attemptToMoveLeft(grid: Grid, block: Block):
    canMove = True
    while(canMove):
        block.move(0, -1)
        if block_inside(grid, block) == False or block_fits(grid, block) == False:
            block.move(0, 1)
            canMove = False

def attemptToMoveRight(grid: Grid, block: Block):
    block.move(0, 1)

def moveDown(grid: Grid, block: Block):
    canMove = True
    while(canMove):
        block.move(1, 0)
        if block_inside(grid, block) == False or block_fits(grid, block) == False:
            block.move(-1, 0)
            canMove = False

def checkValid(grid: Grid, block: Block):
    if block_inside(grid, block) == False or block_fits(grid, block) == False:
        return False
    return True

def block_inside(grid: Grid, block: Block):
    tiles = block.get_cell_positions()
    for tile in tiles:
        if grid.is_inside(tile.row, tile.column) == False:
            return False
    return True

def block_fits(grid: Grid, block: Block):
    tiles = block.get_cell_positions()
    for tile in tiles:
        if grid.is_empty(tile.row, tile.column) == False:
            return False
    return True