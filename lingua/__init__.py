from operator import concat
from random import randint

from numpy import array
import pygame
from pgu import algo, engine

from .entities.player import Player
from .entities.peasant import Peasant, HOMES, TARGETS, WHARFS

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.peasants = []
        self.counter = 0
        # Load map
        self.map = pygame.image.load('assets/map.png')
        self.overlay = pygame.image.load('assets/overlay.png')
        # Load level map
        levels_image = pygame.image.load('assets/levels.png')
        width, height = levels_image.get_size()
        white = pygame.color.Color(255,255,255,255)
        #black = pygame.color.Color(0,0,0,255)
        red = pygame.color.Color(255,0,0,255)
        green = pygame.color.Color(0,255,0,255)
        blue = pygame.color.Color(0,0,255,255)
        #yellow = pygame.color.Color(255,255,0,255)
        self.levels = array([[levels_image.get_at((x,y)) not in [white, green] \
            for y in range(height)] \
            for x in range(width)],
            dtype=bool)
        for x in range(width):
            for y in range(height):
                if levels_image.get_at((x,y)) == red:
                    self.player = Player(self.levels, (x,y))
                elif levels_image.get_at((x,y)) == green:
                    HOMES.append((x,y))
                elif levels_image.get_at((x,y)) == blue:
                    TARGETS.append((x,y))
                    self.peasants.append(Peasant(self.levels, (x,y), self))
        # Populate sprites
        self.sprites = pygame.sprite.RenderPlain([self.player,] + self.peasants)
    
    def loop(self):
        self.screen.blit(self.map, (0,0))
        self.sprites.update()
        self.sprites.draw(self.screen)
        self.screen.blit(self.overlay, (0,0))
        pygame.display.update()
    
    def click(self, target):
        self.player.walk(target)