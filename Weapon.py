#!/usr/bin/env python

# TODO: Subweapons don't support different fire rates

class Weapon():
    def __init__(self, speed=0, radius=0, mass=0, rate=0, angle=0, autofire=False,
                 maxCharge=0, speedCharge=0, radiusCharge=0, massCharge=0,
                 barrel_length=0, spin_speed=0, subweapons=[]):
        """ speed: Bullet launch speed in pixels/second
            radius: Bullet radius in pixels
            mass: Bullet mass in relative units, where most ships are one unit
            rate: Minimum delay between shots
            angle: Offset in radians from the direction of the ship
            autofire: Automatically shoot when fully charged
            maxCharge: Amount of time the weapon can be charged up
            speedCharge: Ratio of speed increase to charge time (pixels/second^2)
            radiusCharge: Ratio of size increase to charge time (pixels/second)
            massCharge: Ratio of mass increase to charge 
            barrel_length: Length of gun barrel relative to ship center in pixels
            spin_speed: Angular velocity of bullet in radians/second
            subweapons: Array of other weapons built into this weapon
        """
        self.speed = speed
        self.radius = radius
        self.mass = mass
        self.rate = rate
        self.angle = angle
        self.autofire = autofire
        self.maxCharge = maxCharge
        self.speedCharge = speedCharge
        self.radiusCharge = radiusCharge
        self.massCharge = massCharge
        self.barrel_length = barrel_length
        self.spin_speed = spin_speed
        self.subweapons = subweapons

    def shoot(self, charge, pose):
        """ Creates new bullets based on the pose of the ship. """
        bullets = []
        # Subweapons
        for weapon in self.subweapons:
            bullets += weapon.shoot(charge, pose)
        # Angular velocity
        pose = pose.getPose(spin_speed=self.spin_speed)
        # Angle
        pose.rotate(self.angle)
        # Position
        pose.translate(pose.direction*self.barrel_length)
        # Velocity
        speed = self.speed + charge*self.speedCharge
        pose.velocity = pose.direction*speed
        # Radius
        radius = self.radius + charge*self.radiusCharge
        # Mass
        mass = self.mass + charge*self.massCharge
        bullets += Bullet(radius, mass, pose)
        return bullets

