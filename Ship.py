#!/usr/bin/env python

class Ship():
    def __init__(self, ship_id, starting_weapon, movement, shape):
        #   Define ship id
        self.id = ship_id

        #   Define weapon based on weapon object
        #   TODO design weapon object
        self.weapon = starting_weapon

        #   Define movement parameters based on movement object
        self.spin_speed = movement.spin_speed
        self.max_speed = movement.max_speed
        self.friction = movement.friction

        #   Define shape parameters based on shape object
        self.mass = shape.mass
        self.radius = shape.radius
        self.barrel_length = shape.barrel_length

class ShipMovement():
    def __init__(self, spin_speed, max_speed, friction):
        #   Define movement parameters based on input
        self.spin_speed = spin_speed
        self.max_speed = max_speed
        self.friction = friction

class ShipShape()
    def __init__(self, mass, radius, barrel_length):
        #   Define shape parameters based on inputs
        self.mass = mass
        self.radius = radius
        self.barrel_length = barrel_length
