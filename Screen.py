#!/usr/bin/env python

import pygame
from Constants import *

class Screen():
    def __init__(self):
        #   Create pygame window TODO make sure pygame is initialized already
        self.disp = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        pygame.display.set_caption("Spinny")    #   TODO Name this better

        self.disp.fill((0, 0, 0))

    def render_screen(self, game):
        """ Renders pygame display based on a game object.
        Inputs: game object. """
        #   TODO this

        for player in game.players:
            self.render_player(player)
        self.flip()

    def render_player(self, player):
        """ Draws a player on the screen.
        Inputs: player object """

        #   Unpack necessary parameters, convert to screen frame
        pos = global_pos_to_screen(player.pose.pos)
        direction = player.pos.direction
        radius = global_scale_to_screen(player.ship.radius)
        barrel_length = global_scale_to_screen(player.ship.barrel_length)
        gun_tip_pos = barrel_length * direction + pos

        #   Barrel width is currently arbitrary number
        barrel_width = global_scale_to_screen(5.0)

        #   TODO change color based on player
        #   TODO Use actual sprites
        body_color = (210, 140, 100)
        gun_color = (180, 120, 80)
        pygame.draw.circle(self.disp, body_color, pos, radius)
        pygame.draw.line(self.disp, gun_color, pos, gun_tip_pos, barrel_width)

    def global_pos_to_screen(self, level, pos):
        """ Converts a position in the global frame to one in the screen
        frame based on the dimensions of the current level.
        Inputs: level object, 2-part position array
        Outputs: new 2-part position array """

        x_pos = pos[0]
        y_pos = pos[1]
        new_x = self.global_scale_to_screen(level, x_pos)
        new_y = self.global_scale_to_screen(level, y_pos)
        return np.asarray([new_x, new_y])

    def global_scale_to_screen(self, level, size):
        """ Converts a scalar from the global frame to the screen frame.
        Inputs: level object, scalar
        Outputs: new scalar """

        scale_factor = float(WINDOW_WIDTH)/level.width
        return size * scale_factor

    def flip(self):
        pygame.display.flip()
