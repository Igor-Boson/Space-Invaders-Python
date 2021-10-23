from entity import Player, Shot, Alien

class Game:
    def __init__(self, handler, speed=10, score=0, max_shots=10, alien_matrix_height=3, alien_matrix_width=4):
        self.handler = handler
        self.speed = speed
        self.score = score
        self.max_shots = max_shots
        self.am_height = alien_matrix_height
        self.am_width = alien_matrix_width
        
        self.alien_list = []
        self.shot_list = []
    
    def create_alien_matrix(self):
        starting_x_value = 100
        starting_y_value = 50
        x_value_increase = 15 + Alien.ALIEN_SIZE
        y_value_increase = 10 + Alien.ALIEN_SIZE
        for w in range(self.am_width):
            for h in range(self.am_height):
                alien = Alien(self.handler, starting_x_value + x_value_increase*w, starting_y_value + y_value_increase*h)
                self.alien_list.append(alien)
    
    def update_player_position(self, key):
        self.handler.player.x += self.handler.player.speed*key
    
    def fire(self):
        if len(self.shot_list) < self.max_shots:
            shot = Shot(self.handler, self.handler.player.x + self.handler.player.size/4, self.handler.player.y)
            self.shot_list.append(shot)
            
    def update_shot_state(self):
        for shot in self.shot_list:
            for alien in self.alien_list:
                if shot.check_collision(alien):
                    shot.health -= 1
                    alien.health -= 1       
            
    def update_shot_positions(self):
        new_shot_list = []
        for shot in self.shot_list:
            if shot.y > 0:
                shot.y -= shot.speed
                new_shot_list.append(shot)
        self.shot_list = new_shot_list
    
    
    def update_alien(self):
        new_alien_list = []
        for alien in self.alien_list:
            alien.move()
            new_alien_list.append(alien)
        self.alien_list = new_alien_list
            
    def update(self, key):
        self.update_player_position(key)
        self.update_alien()
        self.update_shot()
             
    #ainda não ajeitei a enemy_list
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False    
