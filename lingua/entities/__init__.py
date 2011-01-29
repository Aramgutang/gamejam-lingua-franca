import pygame

class Person(pygame.sprite.Sprite):
    def __init__(self, levels):
        super(Person, self).__init__()
        self.levels = levels
        self.path = []
    
    def update(self):
        if self.path:
            new_pos = self.path.pop()
            self.rect.midbottom = new_pos