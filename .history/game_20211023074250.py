from entity import Player
import pygame

class Game:
    def __init__(self, speed=10, score=0):
        self.speed = speed
        self.score = score
        
        self.enemy_list = []
        self.shot_list = []
    
    
    def update_player_position(self, player, key):
        player.x += player.speed*key
    
    #ainda não ajeitei a enemy_list
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False    
