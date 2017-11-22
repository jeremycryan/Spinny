#!/usr/bin/env python

from Bullet import *

class Weapon():
    def __init__(self, speed=0, radius=0, mass=0, cooldown=1, angle=0, autofire=False,
                 charge_time=0, speed_charge=0, radius_charge=0, mass_charge=0,
                 spin_charge=0, barrel_length=0, spin_speed=0):
        """ speed: Bullet launch speed in pixels/second
            radius: Bullet radius in pixels
            mass: Bullet mass in relative units, where most ships are one unit
            cooldown: Minimum delay between shots
            angle: Offset in radians from the direction of the ship
            autofire: Automatically shoot when fully charged
            charge_time: Amount of time to fully charge the weapon
            speed_charge: Speed multiplier of fully charged bullet
            radius_charge: Radius multiplier of fully charged bullet
            mass_charge: Mass multiplier of fully charged bullet
            spin_charge: Ship spin speed multiplier when fully charged
            barrel_length: Length of gun barrel relative to ship center in pixels
            spin_speed: Angular velocity of bullet in radians/second
        """
        self.speed = speed
        self.radius = radius
        self.mass = mass
        self.cooldown = cooldown
        self.angle = angle
        self.autofire = autofire
        self.charge_time = charge_time
        self.speed_charge = speed_charge
        self.radius_charge = radius_charge
        self.mass_charge = mass_charge
        self.spin_charge = spin_charge
        self.barrel_length = barrel_length
        self.spin_speed = spin_speed

    def shoot(self, charge, pose):
        """ Creates new bullets based on the pose of the ship. """
        bullets = []
        # Angular velocity
        pose = pose.getPose(spin_speed=self.spin_speed)
        # Angle
        pose.rotate(self.angle)
        # Position
        pose.translate(pose.direction*self.barrel_length)
        # Velocity
        speed = self.speed*(self.speed_charge**charge)
        pose.vel = pose.direction*speed
        # Radius
        radius = self.radius*(self.radius_charge**charge)
        # Mass
        mass = self.mass*(self.mass_charge**charge)
        return [Bullet(radius, mass, pose)]
