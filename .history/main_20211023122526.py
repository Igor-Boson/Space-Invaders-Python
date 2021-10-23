import sys
import pygame 
from game import Game
from screen import Screen
from entity import Player
from handler import Handler

def play_game(handler):
    #initializing
    game.create_alien_matrix()
    game_over = False

    #running
    while not game_over:
         
        left = False
        right = False
        #AJEITAR O PLAYER MOVEMENT PRA FICAR MAIS FLUIDO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.x > 0:
                    left = True
                if event.key == pygame.K_RIGHT and \
                    player.x < (handler.screen.width - handler.player.size):
                    right = True
                if event.key == pygame.K_SPACE:
                    handler.game.fire()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                             
        game.update(key)
        screen.update_screen()
        
        # if game.collision_check(player):
        #     game_over = True    
        #     break

if __name__ == '__main__':
    pygame.init()
    
    handler = Handler()
    
    game = Game(handler)
    screen = Screen(handler)
    player = Player(handler, screen.width/2, screen.height - 100)
    
    handler.game = game
    handler.screen = screen
    handler.player = player
    
    play_game(handler)