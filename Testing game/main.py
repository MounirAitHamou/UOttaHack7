import pygame,sys
from game import Game
from colors import Colors

class Main:
	def __init__(self):
		self.game = Game()
		self.grid = self.game.grid

	def ai_move(self, position,rotation):
		for i in range(rotation):
			self.game.rotate()
		self.game.move_left()
		for i in range(position):
			self.game.move_right()
		temp = self.game.next_block
		while self.game.current_block != temp:
			self.game.move_down()

	def get_gameState(self):
		return self.game.grid.get_gameState()

main = Main()
main.get_gameState()