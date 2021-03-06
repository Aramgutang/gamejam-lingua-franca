# Credits: Wade Clarke -- music

#import psyco
#psyco.full()

import pygame
from pygame.locals import *

from lingua import Game

pygame.init()
screen = pygame.display.set_mode((800, 600), FULLSCREEN)
pygame.display.set_caption('Lingua Franca')
game = Game(screen)
clock = pygame.time.Clock()

def main():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                game.click(pygame.mouse.get_pos())
            elif event.type == 25:
                game.drop_box()
        game.loop()
    pygame.quit()

if __name__ == '__main__': main()