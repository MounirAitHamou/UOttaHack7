from Game.components.block import Block
from Game.components.blocks import *
from Game.components.game import Game
import random

class Trainer:
    def __init__(self):
        self.game = Game()

    def getRandomPiece(self) -> Block:
        return random.choice([LBlock(), JBlock(), TBlock(), ZBlock(), SBlock(), OBlock(), IBlock()])

    def isGameOver(self) -> bool:
        return self.game.game_over

    def step(self, block: Block) -> int:
        self.game.current_block = block
        while self.game.current_block != self.game.next_block:
            self.game.move_down()