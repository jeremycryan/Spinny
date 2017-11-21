#!/usr/bin/env python

class Bullet:
    def __init__(self, radius, pose):
        self.radius = radius
        self.pose = pose

    def update(self, dt):
        self.pose.update(dt)
