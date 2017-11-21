#!/usr/bin/env python

import pygame

class Screen():
    def __init__(self):
        #   Create pygame window TODO make sure pygame is initialized already
        self.disp = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        pygame.display.set_caption("Spinny")    #   TODO Name this better

    def render_screen(self, game):
        """ Renders pygame display based on a game object.
        Inputs: game object. """
        #   TODO this
