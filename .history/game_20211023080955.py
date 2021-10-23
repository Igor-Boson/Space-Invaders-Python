from entity import Player, Shot
import pygame

class Game:
    def __init__(self, speed=10, score=0, max_shots=10):
        self.handler = None
        self.speed = speed
        self.score = score
        self.max_shots = max_shots
        
        self.enemy_list = []
        self.shot_list = []
    
    def update_player_position(self, key):
        self.handler.player.x += self.handler.player.speed*key
    
    def fire(self):
        if len(self.shot_list) < self.max_shots:
            shot = Shot(self.handler.player.x + self.handler.player.size/2, self.handler.player.y)
            self.shot_list.append(shot)
    
    def update_shot_positions(self):
        new_shot_list = []
        for shot in self.shot_list:
            if shot.y < self.handler.screen.height:
                shot.y -= shot.speed
                new_shot_list.append(shot)
        self.shot_list = new_shot_list
    
    #ainda não ajeitei a enemy_list
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False    
