import threading
import time
import sys
import os

from Shared_Util.Gamestate import GameState
from Shared_Util.Piece import Piece


class Controller:
    def __init__(self):
        self.gameState: GameState = GameState()
    
    def resetGameState(self):
        self.gameState = GameState()
        return self.gameState
    
    def step(self, action: Piece):
        playerPiece = self.gameState.playerPiece
        clockwise_rotations = (action.rotation - playerPiece.rotation) % 4
        counter_clockwise_rotations = (playerPiece.rotation - action.rotation) % 4

        if clockwise_rotations <= counter_clockwise_rotations:
            rotations_needed,direction = clockwise_rotations, 1
        else:
            rotations_needed,direction = counter_clockwise_rotations, -1

        for _ in range(rotations_needed):
            self.gameState.playerPiece.rotate(direction)
            
        
        distance = action.coordinates.x - playerPiece.coordinates.x
        if distance > 0:
            for _ in range(distance):
                self.gameState.playerPiece.move(1)
        else:
            for _ in range(-distance):
                self.gameState.playerPiece.move(-1)



            


       








myController = Controller()
myController.gameState.display()
        
