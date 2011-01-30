import pygame
from pgu.algo import getline
from random import randint, choice

from . import Person
from ..utils import astar, find_closest_path

STARTS = []
HOMES = []
TARGETS = []
WHARFS = [(53, 430), (104, 253), (264, 80)]

ACTIVE_PEASANTS = 40

class Peasant(Person):
    def __init__(self, levels, position, game):
        super(Peasant, self).__init__(levels)
        self.wait()
        self.game = game
        self.home = None
        self.image = pygame.image.load('assets/peasant.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
    
    def wait(self):
        self.waiting = True
        self.wait_counter = randint(60,240)
    
    def walk(self, target):
        self.waiting = False
        self.path = astar(self.rect.midbottom, target, self.levels)
    
    def get_busy(self):
        if len(filter(lambda x: not x.waiting, self.game.peasants)) >= ACTIVE_PEASANTS:
            self.wait()
        else:
            self.walk(filter(lambda x: x != self.rect.midbottom, TARGETS)[randint(0,len(TARGETS)-2)])
    
    def update(self):
        if self.waiting:
            self.wait_counter -= 1
            if not self.wait_counter:
                self.get_busy()
        super(Peasant, self).update()
        if not self.path and tuple(self.rect.midbottom) in WHARFS:
            wharf = WHARFS.index(tuple(self.rect.midbottom))
            box = self.game.wharfs[wharf]
            if box.rect.midbottom != self.rect.midbottom:
                return
            self.game.wharfs[wharf] = None
            self.attach_box(box)
            self.home = choice(HOMES)
            self.walk(find_closest_path(self.home, self.levels))
        elif not self.path and self.box and self.home:
            if tuple(self.rect.midbottom) == self.home:
                self.box.kill()
                self.box = None
                self.path = getline(self.rect.midbottom, find_closest_path(self.home, self.levels))
                self.path.reverse()
            else:
                self.path = getline(self.rect.midbottom, self.home)
                self.path.reverse()
        elif not self.path and not self.waiting:
            self.wait()
