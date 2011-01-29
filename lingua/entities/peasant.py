import pygame

from . import Person
from ..utils import fstar

STARTS = []
HOMES = []
TARGETS = []
WHARFS = []

class Peasant(Person):
    def __init__(self, *args, **kwargs):
        super(Peasant, self).__init__(*args, **kwargs)
        self.target = None
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (455.0, 350.0)
    
    def walk(self, target):
        self.target = None
        self.path = fstar(self.rect.midbottom, target, self.levels)
        if not self.path:
            pass # TODO: Seek another target
        elif self.path[0] != target:
            self.target = target
    
    def update(self):
        super(Peasant, self).update()
        if not self.path and self.target:
            self.walk(self.target)