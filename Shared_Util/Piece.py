from Pieces import Pieces
from Colors import Colors
from Coordinates import Coordinates
from random import random
class Piece:
    def __init__(self,
                 coordinates: Coordinates = Coordinates(0, 0),
                 type: Pieces = Pieces.I,
                 rotation: int = 0):
        self.coordinates = coordinates
        self.type = type
        self.rotation = rotation
        self.color = Colors[self.type]

    def generateRandomPiece(self):
        pass