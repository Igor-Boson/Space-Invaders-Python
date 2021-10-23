from entity import Player
import pygame

class Game:
    def __init__(self, speed=10, score=0):
        self.speed = speed
        self.score = score
        
        self.enemy_list = []
    
    def handle_player_commands(self, player):
        if player.x <= 0:
            key = 0
        if player.x >= (screen.width - player.size):
            key = 0   
        
        for event in pygame.event.get():
            
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
    
    def update_player_position(self, player, key):
        player.x += player.speed*key
    
    #ainda não ajeitei a enemy_list
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False    
