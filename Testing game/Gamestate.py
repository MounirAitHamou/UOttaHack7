from main import *
class Gamestate:

    def __init__(self):
        self.main = main()
        self.gameState = self.main.get_gamestate()
        self.current_piece = self.main.game.current_block
        self.next_piece = self.main.game.next_block
        self.stored_piece = self.main.game.stored_block
        self.score = self.main.game.score

    def get_game_state(self):
        return self.gamestate
    
    def test(self):
        for i in range(19):
            self.main.ai_move(0,0)
            if self.main.game.game_over == True:
                print("game over")
                break
        self.main.grid.print_grid()
        self.main.grid.reset()
        print("reset")
        self.main.grid.print_grid()


game = Gamestate()

game.test()
