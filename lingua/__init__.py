from operator import concat
from random import randint, choice

from numpy import array
import pygame
from pgu import algo, engine
from pgu.algo import getline

from .entities import Box
from .entities.player import Player
from .entities.peasant import Peasant, HOMES, TARGETS, WHARFS

class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.peasants = []
        self.counter = 0
        self.wharfs = [None, None, None]
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
                    self.player = Player(self.levels, (x,y), self)
                elif levels_image.get_at((x,y)) == green:
                    HOMES.append((x,y))
                elif levels_image.get_at((x,y)) == blue:
                    TARGETS.append((x,y))
                    self.peasants.append(Peasant(self.levels, (x,y), self))
        # Populate sprites
        self.sprites = pygame.sprite.RenderPlain([self.player,] + self.peasants)
        # Load images
        self.box = pygame.image.load('assets/box.png')
        self.green_speech = pygame.image.load('assets/green_speech.png')
        # Load sounds
        self.folk_intro = pygame.mixer.Sound('assets/music/waltz_intro.wav')
        self.folk_loop = pygame.mixer.Sound('assets/music/waltz_loop.wav')
        self.rock_loop = pygame.mixer.Sound('assets/music/rock_loop.wav')
        self.folk = pygame.mixer.Channel(0)
        self.rock = pygame.mixer.Channel(1)
        self.rock.set_volume(0.0)
        self.folk.play(self.folk_intro)
        self.rock.play(self.rock_loop, -1)
        # Set up events
        pygame.time.set_timer(25, 4000)
    
    def loop(self):
        if not self.folk.get_queue():
            self.folk.queue(self.folk_loop)
        self.screen.blit(self.map, (0,0))
        self.sprites.update()
        self.sprites.draw(self.screen)
        self.screen.blit(self.overlay, (0,0))
        pygame.display.update()
    
    def click(self, target):
        self.player.yell(self.green_speech)
        self.player.walk(target)
    
    def drop_box(self):
        if None in self.wharfs:
            wharfs = filter(lambda x: not self.wharfs[x], range(3))
            wharf = choice(wharfs)
            box = Box(self.sprites)
            box.image = self.box
            box.rect = box.image.get_rect()
            box.rect.midbottom = [WHARFS[wharf][0], 0]
            box.path = getline(box.rect.midbottom, WHARFS[wharf])
            box.path.reverse()
            self.wharfs[wharf] = box
            peasant = choice(filter(lambda x: not x.box, self.peasants))
            peasant.walk(WHARFS[wharf])
            pygame.time.set_timer(25, 4000)
        else:
            pygame.time.set_timer(25, 2000)
            