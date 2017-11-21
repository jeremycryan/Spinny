#!/usr/bin/env python

class Bullet:
    def __init__(self, radius, mass, pose):
        self.radius = radius
        self.mass = mass
        self.pose = pose

    def update(self, dt):
        self.pose.update(dt)

    def __repr__(self):
        return("Radius: %s, Mass: %s, Pose: %s") % (self.radius, self.mass, self.pose)
