#!/usr/bin/env python

import pygame

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.framerate = 50

        self.players = []

    
