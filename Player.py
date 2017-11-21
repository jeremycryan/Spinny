#!/usr/bin/env python

import numpy as np
import math

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
        self.chargeTime = 0
        self.bullets = []

    def update(self, dt):
        self.pose.update(dt)
        for bullet in self.bullets:
            bullet.update(dt)

    def charge(self, dt):
        """ Charge up a weapon. """
        self.chargeTime = min(self.chargeTime+dt, self.weapon.maxCharge)
        if self.weapon.autofire and self.chargeTime == self.weapon.maxCharge:
            self.shoot(dt)

    def shoot(self, dt):
        """ Fire a weapon if enough cooldown time has elapsed. """
        if self.chargeTime < 0:
            self.chargeTime = min(self.chargeTime+dt,0)
        if self.chargeTime > 0:
            bullets = self.weapon.shoot(self.chargeTime, self.pose)
            self.chargeTime = -self.weapon.rate
            self.pose.velocity = get_impulse(bullets)

    def get_impulse(self, bullets):
        """ Determine the ship velocity based on the projectiles launched """
        velocity = np.asarray((0.0, 0.0))
        for bullet in bullets:
            velocity -= bullet.pose.vel*bullet.mass/self.ship.mass
        return velocity

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
