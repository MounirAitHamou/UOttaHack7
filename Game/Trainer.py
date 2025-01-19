from Game.components.block import Block
from Game.components.blocks import *
from Game.components.game import Game
from random import random

class Trainer:
    def __init__(self):
        self.game = Game()

    def getRandomPiece() -> Block:
        return Block(random.choice([LBlock, JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock]))

    def isGameOver(self) -> bool:
        return self.game.game_over

    def step(self, block: Block) -> int:
        while self.game.current_block != self.game.next_block:
            self.game.move_down()

    def attemptToMoveLeft(self) -> bool:
        return self.game.move_left()
    
    def attemptToMoveRight(self) -> bool:
        return self.game.move_right()

    def lockBlock(self):
        self.game.lock_block()
    
    def moveDown(self):
        while self.game.current_block != self.game.next_block:
            self.game.move_down()
    
    def checkValid(self):
        if self.game.block_inside == False or self.game.block_fits() == False:
            return False
        return True