import sys
import pygame 
from entity import Player
from screen import Screen
from game import Game

def play_game(screen, player, game):
    game_over = False
    key = 'none'
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.x > 0:
                    player.x -= player.size
                if event.key == pygame.K_RIGHT and player.x < (screen.width - player.size):
                    player.x += player.size
                    
            game.update_player_position(player, key)
            # game.drop_enemies(screen.width)
            # game.update_enemy_positions(screen.height)
            # game.set_level()
            
            #screen.update_screen(game.enemy_list, player, game.score)
            screen.update_screen(player)
            
            # if game.collision_check(player):
            #     game_over = True    
            #     break

if __name__ == '__main__':
    pygame.init()
    
    screen = Screen()
    player = Player(screen.width/2, screen.height - 100)
    game = Game()
    
    play_game(screen, player, game)