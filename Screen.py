#!/usr/bin/env python

import pygame
import numpy as np
import math
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

        self.disp.fill((0, 0, 0))
        for player in game.players:
            self.render_player(game.cur_level, player)
            self.render_bullets(game.cur_level, player)
        self.flip()

    def whiten_color(self, color, whiteness=0.0):
        r = color[0]*(1-whiteness) + 255*whiteness
        g = color[1]*(1-whiteness) + 255*whiteness
        b = color[2]*(1-whiteness) + 255*whiteness
        return (int(r), int(g), int(b))

    def render_player(self, level, player):
        """ Draws a player on the screen.
        Inputs: current level object, player object """

        #   Unpack necessary parameters, convert to screen frame
        pos = self.global_pos_to_screen(level, player.pose.pos)
        direction = player.pose.direction
        radius = self.global_scale_to_screen(level, player.ship.radius)

        #   Cast parameters to ints so pygame doesn't shit itself
        pos = pos.astype(int)
        radius = int(radius)

        #   Barrel width is currently arbitrary number
        barrel_width = int(self.global_scale_to_screen(level, 15.0))

        #   TODO change color based on player
        #   TODO Use actual sprites
        chargedness = 0.2
        gun_color = self.whiten_color(player.color, chargedness)
        body_color = (gun_color[0] - 50,
            gun_color[1] - 50,
            gun_color[2] - 50)

        #   Draw player as circle
        pygame.draw.circle(self.disp, body_color, pos, radius)

        #   Draw each weapon as a line
        for weapon in player.weapons:

            #   Determine weapon attributes from weapon object
            barrel_length = self.global_scale_to_screen(level, weapon.barrel_length)
            barrel_length = int(barrel_length)
            gun_tip_pos = (barrel_length * direction)
            rot_mat = np.asarray([[math.cos(weapon.angle), -math.sin(weapon.angle)],
                                [math.sin(weapon.angle), math.cos(weapon.angle)]])
            gun_tip_pos = rot_mat.dot(gun_tip_pos) + pos
            gun_tip_pos = gun_tip_pos.astype(int)

            pygame.draw.line(self.disp, gun_color, pos, gun_tip_pos, barrel_width)

    def render_bullets(self, level, player):
        """ Draws all the bullets fired by player on the screen.
        Input: current level object, player object. """

        #   Iterate through each bullet in list
        for bullet in player.bullets:

            #   Unpack parameters, convert to screen frame
            pos = self.global_pos_to_screen(level, bullet.pose.pos)
            radius = self.global_scale_to_screen(level, bullet.radius)

            #   Cast to ints
            pos = pos.astype(int)
            radius = int(radius)

            bullet_color = player.color
            pygame.draw.circle(self.disp, bullet_color, pos, radius)

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
