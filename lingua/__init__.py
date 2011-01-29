from operator import concat

from numpy import array
import pygame
from pgu import algo, engine

from .entities.player import Player

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        # Load map
        self.map = pygame.image.load('assets/map.png')
        self.overlay = pygame.image.load('assets/overlay.png')
        # Load level map
        levels_image = pygame.image.load('assets/levels.png')
        width, height = levels_image.get_size()
        #white = pygame.color.Color(255,255,255,255)
        black = pygame.color.Color(0,0,0,255)
        self.levels = array([[levels_image.get_at((x,y)) == black \
            for y in range(height)] \
            for x in range(width)],
            dtype=bool)
        # Initialise player
        self.player = Player(self.levels)
        # Populate sprites
        self.sprites = pygame.sprite.RenderPlain((self.player,))
    
    def loop(self):
        self.screen.blit(self.map, (0,0))
        self.sprites.update()
        self.sprites.draw(self.screen)
        self.screen.blit(self.overlay, (0,0))
        pygame.display.update()
    
    def click(self, target):
        self.player.walk(target)