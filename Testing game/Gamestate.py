from main import Main
class Gamestate:
    def __init__(self):
        self.main = Main()
        self.gameState = self.main.get_gameState()
        self.current_piece = self.main.game.current_block
        self.next_piece = self.main.game.next_block
        self.stored_piece = self.main.game.stored_block
        self.score = self.main.game.score
        self.game_over = self.main.game.game_over

    def get_gameState(self):
        return self.gameState
    
    def reset(self):
        self.main.grid.reset()
    
    def move(self, position, rotation):
        if not self.game_over:
            self.main.ai_move(position, rotation)
        if self.game_over == True:
            print("game over")


game = Gamestate()

game.move(0,3)
game.main.grid.print_grid()
