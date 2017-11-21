#!/usr/bin/env python

import numpy as np
import math

class Pose:
    def __init__(self, pos=(0,0), vel=(0,0), direction=(1,0), spin_speed=0):
        """ pos: Position vector in world frame in pixels
            vel: Velocity vector in world frame in pixels/second
            direction: Direction unit vector in world frame
            spin_speed: Angular velocity in radians/second """
        self.pos = np.asarray(pos).astype(float)
        self.vel = np.asarray(vel).astype(float)
        self.direction = np.asarray(direction).astype(float)
        self.spin_speed = spin_speed

    def getPose(self, **args):
        """ Constructs a new pose with any unspecified parameters
        copied from this pose. """
        for key, val in vars(self).items():
            if not key in args:
                args[key] = val
        return Pose(**args)

    def update(self, dt):
        """ Updates position and direction by a given timestep. """
        self.translate(self.vel*dt)
        self.rotate(self.spin_speed*dt)

    def translate(self, displacement):
        """ Translates the pose in the global frame. """
        self.pos += displacement

    def rotate(self, angle):
        """ Rotates the pose counterclockwise by an angle in radians. """
        rot_mat = np.asarray([[math.cos(angle), -math.sin(angle)],
                            [math.sin(angle), math.cos(angle)]])
        new_direction = rot_mat.dot(self.direction)
        self.direction = new_direction/np.linalg.norm(new_direction)

    def __repr__(self):
        return("Position: %s, Direction: %s") % (self.pos, self.direction)
