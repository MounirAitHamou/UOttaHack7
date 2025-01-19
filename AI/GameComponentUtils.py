import copy
from Game.components.block import Block

def cloneBlock(block: Block) -> Block:
    return copy.deepcopy(block)