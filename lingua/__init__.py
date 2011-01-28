import pygame
from pgu import algo, engine

from .entities.player import Player

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        # Load map
        self.map = pygame.image.load('assets/map.tga')
        # Load level map
        levels_image = pygame.image.load('assets/levels.tga')
        width, height = levels_image.get_size()
        white = pygame.color.Color(255,255,255,255)
        self.levels = [[levels_image.get_at((x,y)) != white \
            for x in range(width)] \
            for y in range(height)]
        # Initialise player
        self.player = Player()
        # Populate sprites
        self.sprites = pygame.sprite.RenderPlain((self.player,))
    
    def loop(self):
        self.screen.blit(self.map, (0,0))
        self.sprites.update()
        self.sprites.draw(self.screen)
        pygame.display.update()
    
    def click(self, x, y):
        self.player.rect.midbottom = (x,y)