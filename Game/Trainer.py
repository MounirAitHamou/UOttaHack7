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