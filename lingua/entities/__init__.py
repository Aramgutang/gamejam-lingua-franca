import pygame

class Box(pygame.sprite.Sprite):
    def update(self):
        if hasattr(self, 'path') and self.path:
            new_pos = self.path.pop()
            self.rect.midbottom = new_pos

class Person(pygame.sprite.Sprite):
    def __init__(self, levels):
        super(Person, self).__init__()
        self.levels = levels
        self.path = []
        self.box = None
        self.bubble = None
    
    def update(self):
        if self.path:
            new_pos = self.path.pop()
            self.rect.midbottom = new_pos
        if self.box:
            self.box.rect.center = self.rect.center
        if self.bubble:
            self.bubble.rect.midbottom = self.rect.midtop
            
    def attach_box(self, box):
        if self.box:
            self.box.kill()
        self.box = box
        self.box.rect.center = self.rect.center
        return self.box
    
    def yell(self, bubble):
        if self.bubble:
            self.bubble.kill()
        self.bubble = pygame.sprite.Sprite()
        self.bubble.image = bubble
        self.bubble.rect = self.bubble.image.get_rect()
        self.bubble.rect.midbottom = self.rect.midtop
        self.groups()[0].add(self.bubble)