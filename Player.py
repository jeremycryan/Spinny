#!/usr/bin/env python

import numpy as np
import math
import pygame

# TODO: Add powerup dictionary

class Player():
    def __init__(self, player_id, ship, controls, pose, color = (100, 100, 100)):
        #   Define player id
        self.id = player_id

        #   Define control scheme based on control object
        self.controls = controls

        #   Define gameplay parameters based on ship and weapon objects
        self.ship = ship
        self.weapons = {weapon:0 for weapon in ship.starting_weapons}
        self.pose = pose
        self.bullets = []
        self.color = color

    def update(self, dt):
        """ Update pose by a timestep. """
        self.pose.spin_speed = self.ship.spin_speed
        for weapon, charge in self.weapons.items():
            self.pose.spin_speed *= weapon.spin_charge**charge
        self.pose.update(dt)
        for bullet in self.bullets:
            bullet.update(dt)

    def charge(self, dt):
        """ Charge up weapons. """
        impulse = np.asarray(0.0, 0.0)
        for weapon, charge in self.weapons.items():
            if charge < 0: # Cooldown
                self.weapons[weapon] = min(charge+dt/weapon.cooldown, 0)
            elif weapon.charge_time==0: # Non-chargeable
                self.weapons[weapon] = 1
            else: # Charging
                self.weapons[weapon] = min(charge+dt/weapon.charge_time, 1)
            if weapon.autofire and charge == 1: # Fully charged
                impulse += self.shoot(weapon)
                self.pose.vel = impulse

    def release(self, dt):
        """ Fire weapons if enough cooldown time has elapsed. """
        impulse = np.asarray(0.0, 0.0)
        for weapon, charge in self.weapons.items():
            if charge < 0: # Cooldown
                self.weapons[weapon] = min(charge+dt/weapon.cooldown, 0)
            if charge > 0: # Shoot
                impulse += self.shoot(weapon)
                self.pose.vel = impulse

    def shoot(self, weapon):
        """ Fire a given weapon and return the resultant ship velocity. """
        bullets = weapon.shoot(self.weapons[weapon], self.pose)
        self.weapons[weapon] = -1
        self.bullets += bullets
        return self.get_impulse(bullets)

    def get_impulse(self, bullets):
        """ Determine the ship velocity based on the projectiles launched. """
        velocity = np.asarray((0.0, 0.0))
        for bullet in bullets:
            velocity -= bullet.pose.vel*bullet.mass/self.ship.mass
        return velocity

    def get_max_charge(self):
        """ Determine the highest charge level of any weapon on the ship.
        Charge of -1 = cooldown, 0 = uncharged, 1 = fully charged. """
        return max(self.weapons.values())

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
