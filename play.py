import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Lingua France')

def main():
    running = True
    while running:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__': main()