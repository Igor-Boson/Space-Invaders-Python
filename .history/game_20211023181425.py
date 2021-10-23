from entity import Player, Shot, Alien
import pygame

class Game:
    def __init__(self, handler, speed=10, score=0, max_shots=10, alien_matrix_height=3, alien_matrix_width=4, fire_delay=0.4):
        self.handler = handler
        self.speed = speed
        self.score = score
        self.max_shots = max_shots
        self.am_height = alien_matrix_height
        self.am_width = alien_matrix_width
        
        #create alien matrix function
        self.starting_x_value = 100
        self.starting_y_value = 50
        self.x_value_increase = 10 + Alien.ALIEN_SIZE
        self.y_value_increase = 10 + Alien.ALIEN_SIZE
        
        #fire function
        self.fire_delay = fire_delay
        self.fire_clock = None
        
        self.alien_list = []
        self.shot_list = []
    
    def create_alien_matrix(self):
        for w in range(self.am_width):
            for h in range(self.am_height):
                alien = Alien(self.handler, \
                            self.starting_x_value + self.x_value_increase*w, \
                            self.starting_y_value + self.y_value_increase*h)
                self.alien_list.append(alien)
    
    def update_player_position(self, left, right):
        if left and self.handler.player.x > 0:
            self.handler.player.x -= self.handler.player.speed
        if right and self.handler.player.x < (self.handler.screen.width - self.handler.player.size):
            self.handler.player.x += self.handler.player.speed
    
    def fire(self):
        if self.fire_clock == None:
            pass
        elif (pygame.time.get_ticks() - self.fire_clock) <= self.fire_delay*1000:
            return
        if len(self.shot_list) < self.max_shots:
            shot = Shot(self.handler, self.handler.player.x + self.handler.player.size/4, self.handler.player.y)
            self.shot_list.append(shot)
            self.fire_clock = pygame.time.get_ticks()
            
    def update_shot(self):
        for shot in self.shot_list:
            for alien in self.alien_list:
                if shot.detect_collision(alien):
                    shot.health -= 1
                    alien.health -= 1       

        new_shot_list = []
        for shot in self.shot_list:
            if shot.y > 0 and shot.health > 0:
                shot.y -= shot.speed
                new_shot_list.append(shot)
        self.shot_list = new_shot_list
    
    
    def update_alien(self):
        new_alien_list = []
        for alien in self.alien_list:
            if alien.health > 0:
                alien.move()
                new_alien_list.append(alien)
            else:
                self.score += alien.score_value
        self.alien_list = new_alien_list
            
    def update(self, left, right):
        self.update_player_position(left, right)
        self.update_shot()
        self.update_alien()
             
    #ainda não ajeitei a enemy_list
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False    
