#!/usr/bin/env python

import pygame
import sys
from Screen import *
from Level import *

class Game():
    def __init__(self):
        #   Initialize pygame
        pygame.init()
        pygame.mixer.init()

        self.framerate = 50
        self.clock = pygame.time.Clock()

        self.players = []
        self.cur_level = Level([1280, 960])

        self.screen = Screen()


if __name__ == '__main__':
    a = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
