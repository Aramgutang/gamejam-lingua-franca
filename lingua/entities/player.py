import pygame
from pgu.algo import getline

from . import Person
from ..utils import astar, find_closest_path

class Player(Person):
    def __init__(self, levels, position=(455.0, 350.0)):
        super(Player, self).__init__(levels)
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
    
    def walk(self, target):
        if not self.levels[target[0], target[1]]:
            target = find_closest_path(target, self.levels)
        self.path = astar(self.rect.midbottom, target, self.levels)
        if not self.path:
            self.path = getline(self.rect.midbottom, target)
            self.path.reverse()
