import pygame,sys
from TetrisGame.components.game import Game
from TetrisGame.components.colors import Colors

class Controller:
    def startGame():
        pause = False
        pygame.init()
        temp1 = None
        title_font = pygame.font.Font(None, 40)
        score_surface = title_font.render("Score", True, Colors.white)
        next_surface = title_font.render("Next", True, Colors.white)
        stored_surface = title_font.render("Stored", True, Colors.white)
        game_over_surface = title_font.render("GAME OVER", True, Colors.white)

        score_rect = pygame.Rect(630, 100, 170, 80)
        next_rect = pygame.Rect(630, 255, 170, 180)
        stored_rect = pygame.Rect(630, 480, 170, 180)

        screen = pygame.display.set_mode((1000, 800))
        img = pygame.image.load("..\TetrisGame\Images\Room.png")
        img = pygame.transform.scale(img, (1000, 800))
        sky = pygame.image.load("..\TetrisGame\Images\Sky.png")
        sky = pygame.transform.scale(sky, (next_rect.width, next_rect.height))
        hangar = pygame.image.load("..\TetrisGame\Images\Hangar.png")
        hangar = pygame.transform.scale(hangar, (stored_rect.width, stored_rect.height))

        r1 = img.get_rect()
        r1.center = screen.get_rect().center
        pygame.display.set_caption("Python Tetris")

        clock = pygame.time.Clock()


        

        game = Game()




        GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(GAME_UPDATE, 200)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if game.game_over == True:
                        game.game_over = False
                        game.reset()
                    if event.key == pygame.K_LEFT and game.game_over == False:
                        game.move_left()
                    if event.key == pygame.K_RIGHT and game.game_over == False:
                        game.move_right()
                    if event.key == pygame.K_DOWN and game.game_over == False:
                        game.move_down()
                    if event.key == pygame.K_UP and game.game_over == False:
                        game.rotate()
                    if event.key == pygame.K_2 and game.game_over == False:
                        game.doAiMove()
                    if event.key == pygame.K_1 and game.game_over == False:
                        if temp1 != game.current_block:
                            game.store_block()
                            temp1 = game.current_block
                    if event.key == pygame.K_9 and game.game_over == False:
                        pause = not pause
                    if event.key == pygame.K_SPACE and game.game_over == False:
                        temp = game.next_block
                        while game.current_block != temp:
                            game.move_down()
                if event.type == GAME_UPDATE and game.game_over == False:
                    if pause != True:
                        game.move_down()
            if temp1 != game.current_block:
                temp1 = None
            score_value_surface = title_font.render(str(game.score), True, Colors.white)
            score_text_surface = title_font.render("Lines Cleared", True, Colors.white)
            next_value_surface = title_font.render("Incoming", True, Colors.white)
            stored_value_surface = title_font.render("Stored", True, Colors.white)

            screen.fill(Colors.dark_blue)
            screen.blit(score_surface, (630, 20, 50, 50))
            screen.blit(next_surface, (630, 500, 50, 50))
            screen.blit(stored_surface, (630, 405, 50, 50))
            screen.blit(img,r1)

            if game.game_over == True:
                screen.blit(game_over_surface, (320, 450, 50, 50))
            bg = pygame.Rect(50, 50, 800, 750)
            bgOutline1 = pygame.Rect(50,50,840,790)
            bg.center = screen.get_rect().center
            bgOutline1.center = screen.get_rect().center
            pygame.draw.rect(screen, (0,0,0), bgOutline1)
            pygame.draw.rect(screen, (31,29,29), bg)
            scoreRect = pygame.Rect(10, 10, 170, 60)
            scoreOut1 = pygame.Rect(10,10, 175, 65)
            scoreOut2 = pygame.Rect(10,10, 180, 70)
            scoreRect.center = score_rect.center
            scoreOut1.center = score_rect.center
            scoreOut2.center = score_rect.center
            pygame.draw.rect(screen, (206,198,198),scoreOut2)
            pygame.draw.rect(screen, (0, 0, 0),scoreOut1)
            pygame.draw.rect(screen, Colors.white, scoreRect)

            colour_rect = pygame.Surface( ( 2, 2 ) )                                 
            pygame.draw.line( colour_rect, (206,198,198),  ( 0,1 ), ( 1,1 ) )            
            pygame.draw.line( colour_rect, (104,100,100), ( 0,0 ), ( 1,0 ) )            
            colour_rect = pygame.transform.smoothscale( colour_rect, ( scoreRect.width, scoreRect.height ) )  
            screen.blit( colour_rect, scoreRect )  


            screen.blit(score_text_surface, score_text_surface.get_rect(centerx = score_rect.centerx, 
                centery = score_rect.centery - 50))
            screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
                centery = score_rect.centery))
            screen.blit(next_value_surface, next_value_surface.get_rect(centerx = next_rect.centerx, 
                centery = next_rect.centery - 110))
            screen.blit(stored_value_surface, stored_value_surface.get_rect(centerx = stored_rect.centerx, 
                centery = stored_rect.centery - 110))
            r2 = sky.get_rect()
            r2.center = next_rect.center
            r3 = hangar.get_rect()
            r3.center = stored_rect.center
            screen.blit(sky,r2)
            screen.blit(hangar,r3)
            game.draw(screen)

            pygame.display.update()
            clock.tick(60)
