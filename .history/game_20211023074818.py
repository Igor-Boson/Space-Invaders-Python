from entity import Player, Shot
import pygame

class Game:
    def __init__(self, speed=10, score=0, max_shots=10):
        self.speed = speed
        self.score = score
        self.max_shots = max_shots
        
        self.enemy_list = []
        self.shot_list = []
    
    def update_player_position(self, player, key):
        player.x += player.speed*key
    
    def shot(self, player):
        if len(self.shot_list) < self.max_shots:
            shot = self.Shot(player.x, player.y)
            self.shot_list.append(shot)
    
    #ainda não ajeitei a enemy_list
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False    
