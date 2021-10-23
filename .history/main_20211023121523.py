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
    key = 0

    #running
    while not game_over:
        
        if handler.player.x <= 0:
            key = 0
        if handler.player.x >= (handler.screen.width - handler.player.size):
            key = 0   
        
        #AJEITAR O PLAYER MOVEMENT PRA FICAR MAIS FLUIDO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.x > 0:
                    key -= 1
                if event.key == pygame.K_RIGHT and \
                    player.x < (handler.screen.width - handler.player.size):
                    key += 1
                if event.key == pygame.K_SPACE:
                    handler.game.fire()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key = 0
                if event.key == pygame.K_RIGHT:
                    key  = 0
                    
                             
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