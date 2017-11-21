#!/usr/bin/env python

import numpy as np
import math
import pygame

class Player():
    def __init__(self, player_id, ship, controls, pose):
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
        self.pose = pose

    def update(self, dt):
        self.pose.update(dt)

class Controls():
    def __init__():
        pass
