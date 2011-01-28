import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.midbottom = self.image.get_size()
#        self.x_offset, self.y_offset = self.image.get_size()
#        self.x_offset //= 2
#        self.y_offset *= -1