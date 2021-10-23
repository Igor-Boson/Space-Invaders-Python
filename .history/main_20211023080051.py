import sys
import pygame 
from game import Game
from screen import Screen
from entity import Player
from handler import Handler

def play_game(game, screen, player):
    game_over = False
    key = 0
    while not game_over:
        
        if player.x <= 0:
            key = 0
        if player.x >= (screen.width - player.size):
            key = 0   
        
        #AJEITAR O PLAYER MOVEMENT PRA FICAR MAIS FLUIDO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.x > 0:
                    key -= 1
                if event.key == pygame.K_RIGHT and player.x < (screen.width - player.size):
                    key += 1
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    key = 0
                if event.key == pygame.K_RIGHT:
                    key  = 0
                    
                             
        game.update_player_position(key)
        # game.drop_enemies(screen.width)
        # game.update_enemy_positions(screen.height)
        # game.set_level()
        
        #screen.update_screen(game.enemy_list, player, game.score)
        screen.update_screen()
        
        # if game.collision_check(player):
        #     game_over = True    
        #     break

if __name__ == '__main__':
    pygame.init()
    
    game = Game()
    screen = Screen()
    player = Player(screen.width/2, screen.height - 100)
    
    handler = Handler(game, screen, player)
    
    game.handler = handler
    screen.handler = handler
    player.handler = handler
    
    play_game(game, screen, player)