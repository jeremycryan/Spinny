#!/usr/bin/env python

import pygame
import sys
import math
from Ship import *
from Player import *
from Pose import *
from Screen import *
from Level import *
from Weapon import *

class Game():
    def __init__(self):
        #   Initialize pygame
        pygame.init()
        pygame.mixer.init()

        self.framerate = 50
        self.clock = pygame.time.Clock()

        p1weapon = Weapon()
        p1movement = ShipMovement(2*math.pi, 30, 0.2)
        p1shape = ShipShape(50, 30, 50)
        p1ship = Ship(1, p1weapon, p1movement, p1shape)
        p1pose = Pose(pos = (800.0, 600.0), spin_speed = 2*math.pi)
        p1 = Player(1, p1ship, 0, p1pose)

        self.players = [p1]
        self.cur_level = Level([1280, 960])

        self.screen = Screen()

    def run(self):
        self.clock.tick()
        while True:
            dt = self.clock.tick(50)/1000.0
            print(dt)
            for player in self.players:
                player.update(dt)
            self.screen.render_screen(self)
            self.check_for_exit()

    def check_for_exit(self):
        """  Checks to see whether user has exited game. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    a = Game()
    a.run()
