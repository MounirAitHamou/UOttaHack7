from Game.components.colors import Colors
import pygame
from Game.components.position import Position

class Block:
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cell_size = 35
		self.row_offset = 0
		self.column_offset = 0
		self.rotation_state = 0
		self.colors = Colors.get_cell_colors()

	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns

	def resetOffset(self):
		self.row_offset = 0
		self.column_offset = 0

	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state]
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0

	def undo_rotation(self):
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

	def draw(self, screen, offset_x, offset_y, outline):
		if not outline:
			tiles = self.get_cell_positions()
			for tile in tiles:
				tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
					offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
				pygame.draw.rect(screen, self.colors[self.id], tile_rect)
				colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
				pygame.draw.line( colour_rect, (206,198,198),  ( 0,1 ), ( 1,1 ) )            # left colour line
				pygame.draw.line( colour_rect, (104,100,100), ( 0,0 ), ( 1,0 ) )            # right colour line
				colour_rect = pygame.transform.smoothscale( colour_rect, ( tile_rect.width, tile_rect.height ) )  # stretch!
				screen.blit( colour_rect, tile_rect ) 
		else:
			tiles = self.get_cell_positions()
			for tile in tiles:
				tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
					offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
				pygame.draw.rect(screen, Colors.light_blue, tile_rect, 3)

