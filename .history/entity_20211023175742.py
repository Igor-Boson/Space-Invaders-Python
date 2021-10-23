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
    def __init__(self, handler, x, y):
        super().__init__(handler, x, y, size=50, color=Color.BLUE, speed=None)
        #o speed nessa classe é utilizado de outra maneira
        self.movement_counter = 0  
        self.score_value = 10
          
    def move(self):
        self.movement_counter += 1
        if self.movement_counter == self.handler.screen.clock_tick:
            #self.x += self.size + Game.ALIENMATRIX_HORIZONTAL_GAP
            self.movement_counter = 0