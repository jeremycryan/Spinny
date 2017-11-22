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
from ShipSelect import *

class Game():
    def __init__(self):
        #   Initialize pygame
        pygame.init()
        pygame.mixer.init()

        self.framerate = 50
        self.clock = pygame.time.Clock()

        p1pose = Pose(pos = (200, 200))
        p1controls = Controls([pygame.K_q])
        p2pose = Pose(pos = (2000.0, 1200.0))
        p2controls = Controls([pygame.K_p])
        p3pose = Pose(pos = (200.0, 1200.0))
        p3controls = Controls([pygame.K_SPACE])
        p1 = Player(1, SHIP_1, p1controls, p1pose, color=(220, 90, 110))
        p2 = Player(2, SHIP_2, p2controls, p2pose, color=(120, 210, 150))
        p3 = Player(3, SHIP_3, p3controls, p3pose, color=(140, 110, 210))

        self.players = [p1, p2, p3]
        self.cur_level = Level([1280*2, 960*2])

        self.screen = Screen()

    def run(self):
        self.clock.tick()
        while True:
            #   Loads pygame events
            pygame.event.pump()
            dt = self.clock.tick(50)/1000.0 # time step in seconds

            #   Handles player charging and shooting
            self.player_shooting(dt)

            #   Updates player positions and angles
            for player in self.players:
                player.update(dt)

            #   Renders screen
            self.screen.render_screen(self)
            self.check_for_exit()

    def player_shooting(self, dt):
        """ Calls players' shoot methods if shoot key is pressed. """

        for player in self.players:
            if player.controls.key_down(player.controls.shoot_key):
                player.charge(dt)
            else:
                player.release(dt)

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
