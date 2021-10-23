from color import Color
import pygame

class Entity:
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.life = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def detect_collision(self, other):
        if (other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)):
            if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + self.size)):
                return True
        return False

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=Color.RED, speed=10)
        
class Shot(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, size=25, color=Color.YELLOW, speed=10)