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
    def __init__(self, key_list):
        self.shoot_key = key_list[0]

    def key_down(self, key):
        """ Checks to see whether a given key is held down. """
        pressed = pygame.key.get_pressed()
        return pressed[key]

    def key_press(self, key):
        """ Checks to see whether a given key has been pressed
        in the time step. """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False

    def key_release(self, key):
        """ Checks to see whether a given key has been released
        in the time step. """
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == key:
                return True
        return False
