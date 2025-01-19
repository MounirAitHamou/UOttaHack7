from Game.components.grid import Grid
from Game.components.blocks import *
import Game.components.block
import random
import pygame
import os
import copy

class Game:
	def __init__(self):
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.recommendation = copy.copy(self.current_block)
		self.stored_block = None
		self.game_over = False
		self.score = 0
		aiRecommendation = [3,1]
		for i in range(aiRecommendation[1]):
			self.recommendation.rotate()
		self.recommendation.move(1, aiRecommendation[0])

	def update_score(self, lines_cleared):
		self.score+= lines_cleared

	def store_block(self):
		if self.stored_block == None:
			self.current_block.resetOffset()
			self.stored_block = self.current_block
			self.current_block = self.next_block
			self.next_block = self.get_random_block()
		else:
			temp = self.stored_block
			self.current_block.resetOffset()
			self.stored_block = self.current_block
			self.current_block = temp

	def get_random_block(self):
		if len(self.blocks) == 0:
			self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		block = random.choice(self.blocks)
		self.blocks.remove(block)
		block.resetOffset()
		return block

	def move_left(self):
		self.current_block.move(0, -1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	def move_right(self):
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)

	def move_down(self):
		self.current_block.move(1, 0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)
			self.lock_block()
		self.grid.get_game_state()

	def lock_block(self):
		tiles = self.current_block.get_cell_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_block.id
		self.current_block = self.next_block
		self.recommendation = copy.copy(self.current_block)
		self.setRecommendation([3,0])
		self.next_block = self.get_random_block()
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.update_score(rows_cleared)
		if self.block_fits() == False:
			self.game_over = True

	def reset(self):
		self.grid.reset()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.score = 0

	def block_fits(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False
		return True

	def rotate(self):
		self.current_block.rotate()
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.undo_rotation()

	def block_inside(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False
		return True
	
	def setRecommendation(self,aiRecommendation):
		for i in range(aiRecommendation[1]):
			self.recommendation.rotate()
		self.recommendation.move(1, aiRecommendation[0])

	def draw(self, screen):
		self.grid.draw(screen)
		self.current_block.draw(screen, 175, 50, 0)
		self.recommendation.draw(screen, 175, 50, 1)

		if self.next_block.id == 3:
			self.next_block.draw(screen, 645, 290, 0)
		elif self.next_block.id == 4:
			self.next_block.draw(screen, 685, 310, 0)
		else:
			self.next_block.draw(screen, 665, 310, 0)

		if self.stored_block != None:
			if self.stored_block.id == 3:
				self.stored_block.draw(screen, 645, 525, 0)
			elif self.stored_block.id == 4:
				self.stored_block.draw(screen, 680, 540, 0)
			else: 
				self.stored_block.draw(screen, 660, 545, 0)