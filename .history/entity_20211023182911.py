from color import Color
import pygame

class Entity:
    def __init__(self, handler, x, y, size, color, speed):
        self.handler = handler
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.health = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def detect_collision(self, other):
        return pygame.Rect(self.x, self.y, self.size, self.size).colliderect(pygame.Rect(other.x, other.y, other.size, other.size))

    # def detect_collision(self, other):
    #     if (other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)):
    #         if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + self.size)):
    #             return True
    #     return False

class Player(Entity):
    def __init__(self, handler, x, y):
        super().__init__(handler, x, y, size=50, color=Color.RED, speed=10)

class Shot(Entity):
    def __init__(self, handler, x, y):
        super().__init__(handler, x, y, size=25, color=Color.YELLOW, speed=10)

class Alien(Entity):
    ALIEN_SIZE = 50
    def __init__(self, handler, x, y, starting_speed=1.0, speed_increase_factor=1.0):
        super().__init__(handler, x, y, size=50, color=Color.BLUE, speed=None)
        #o speed nessa classe é utilizado de outra maneira
        self.tick_counter = 0  
        self.movement_counter = 0
        self.starting_speed = starting_speed
        self.speed_increase_factor = speed_increase_factor
        self.direction = 1
        
        self.score_value = 10
        
        # amount of steps the alien should take before moving down
        self.movement_cap = round((self.handler.screen.width - 2*self.handler.game.starting_x_value\
                            - self.handler.game.am_width*self.size - (self.handler.game.am_width - 1)*(self.handler.game.x_value_increase - self.size))\
                            /(self.size + self.handler.game.x_value_increase))
          
    # the aliens first move all the all to the right
    # then go down, swap direction, and repeat
    # their speed should gradually as they go down the screen      
    def move(self):
        # their movement shouldn't be "continuous", like the player's cannon
        # they should move in "leaps", and after a delay, move again, like in the original game
        
        self.tick_counter += 1
        
        if self.tick_counter == self.handler.screen.clock_tick:     
            # checks if it should go sideways or downwards
            if self.movement_counter < self.movement_cap:   
            # goes sideways
                self.x += self.handler.game.x_value_increase*self.direction
                self.tick_counter = 0
                self.movement_counter += 1
            else:
            # goes downwards, resets the movement counter, and swaps direction
                self.y += self.handler.game.y_value_increase*self.direction
                self.direction *= -1
                self.movement_counter = 0               
                self.tick_counter = 0