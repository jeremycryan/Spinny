#!/usr/bin/env python

import numpy as np
import math

class Player():
    def __init__(self, player_id, ship, controls, position, direction):
        #   Define player id
        self.id = player_id

        #   Define control scheme based on control object
        #   TODO define control object
        self.controls = controls

        #   Define gameplay parameters based on ship and weapon objects
        #   TODO design ship object
        #   TODO design weapon object
        self.ship = ship
        self.weapon = ship.starting_weapon

        #   Define starting orientation based on initialization inputs
        self.pos = np.assarray(position)
        self.direction = np.asarray(direction)

    def rotate_cc(self, amt):
        """ Rotates the ship some amount counterclockwise.
        Input: rotation amount in radians. """

        rot_mat = np.asarray([[math.cos(amt), -math.sin(amt)],
                            [math.sin(amt), math.cos(amt)]])
        new_direction = np.matmul(rot_mat, self.direction)
        self.direction = new_direction/np.norm(new_direction)

    def spin_step(self, dt):
        """ Updates the rotational orientation of the ship based on its current
        spinning speed and a time step.
        Input: time difference since last update, in seconds. """

        rot_amt = self.ship.spin_speed * dt
        self.rotate_cc(rot_amt)
