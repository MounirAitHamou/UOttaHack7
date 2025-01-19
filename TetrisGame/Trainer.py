from TetrisGame.components.block import Block
from TetrisGame.components.blocks import *
from TetrisGame.components.game import Game
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
        original_score = self.game.score
        while self.game.current_block == block:
            self.game.move_down()
        return self.game.score - original_score