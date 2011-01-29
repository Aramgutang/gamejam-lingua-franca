import pygame
from random import randint

from . import Person
from ..utils import astar

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
        self.target = None
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
    
    def wait(self):
        self.waiting = True
        self.wait_counter = randint(60,240)
    
    def walk(self, target):
        self.target = None
        self.waiting = False
        self.path = astar(self.rect.midbottom, target, self.levels)
        if self.path and self.path[0] != target:
            self.target = target
    
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
        if not self.path and self.target:
            self.walk(self.target)
        elif not self.path and not self.waiting:
            self.wait()