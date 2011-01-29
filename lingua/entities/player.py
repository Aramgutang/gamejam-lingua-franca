import pygame
from pgu.algo import astar, getline

from ..utils import aramstar, find_closest_path

class Player(pygame.sprite.Sprite):
    def __init__(self, levels):
        super(Player, self).__init__()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        #self.rect.midbottom = self.image.get_size()
        self.rect.midbottom = (100,100)
        self.levels = levels
        self.path = []
    
    def walk(self, target):
        if not self.levels[target[0], target[1]]:
            target = find_closest_path(target, self.levels)
        self.path = aramstar(self.rect.midbottom, target, self.levels)
        if not self.path:
            self.path = getline(self.rect.midbottom, target)
            self.path.reverse()
    
    def update(self):
        if self.path:
            new_pos = self.path.pop()
            self.rect.midbottom = new_pos