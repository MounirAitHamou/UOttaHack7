import pygame,sys
from game import Game
from colors import Colors

pygame.init()
game = Game()
grid = game.grid

def ai_move(position,rotation):
	for i in range(position):
		game.move_right()
	for i in range(rotation):
		game.rotate()
	temp = game.next_block
	while game.current_block != temp:
		game.move_down()

GAME_UPDATE = pygame.USEREVENT
for i in range(20):
	game.move_down()

grid.print_grid()

if game.game_over == True:
		print("game over")
		grid.print_grid()
