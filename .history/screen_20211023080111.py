from color import Color
import pygame

class Screen:
    def __init__(self, width=800, height=600, background_color=Color.BLACK, font_type="monospace", font_size=35, clock_tick=60):
        self.handler = None
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick
        
    def refresh_background(self):
        self.screen.fill(self.background_color)
        
    def draw_player(self):
        self.handler.player.draw(self.screen)
        
    def update_screen(self):
        self.refresh_background()
        #self.draw_enemies(enemy_list)
        self.draw_player()
        #self.draw_score_label(score)

        self.clock.tick(self.clock_tick)
        pygame.display.update()    