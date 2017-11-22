#!/usr/bin/env python

import numpy as np
from Ship import *
from Weapon import *

MACHINE_GUN = Weapon(barrel_length = 50,
                        mass = 20,
                        speed = 500,
                        radius = 10,
                        rate = 0.2,
                        angle = 0,
                        autofire = True,
                        max_charge = 0.01,
                        speed_charge = 500,
                        radius_charge = 20)

SNIPER = Weapon(barrel_length = 75,
                        mass = 8,
                        speed = 800,
                        radius = 8,
                        rate = 1,
                        angle = 0,
                        autofire = False,
                        max_charge = 3,
                        speed_charge = 500,
                        radius_charge = 8)

STANDARD_GUN = Weapon(barrel_length = 50,
                        mass = 30,
                        speed = 500,
                        radius = 15,
                        rate = 0.5,
                        angle = 0,
                        autofire = False,
                        max_charge = 1,
                        speed_charge = 500,
                        radius_charge = 8)

DOUBLE_GUN = Weapon(barrel_length = 50,
                        mass = 30,
                        speed = 500,
                        radius = 15,
                        rate = 0.5,
                        angle = np.pi/2,
                        autofire = False,
                        max_charge = 1,
                        speed_charge = 500,
                        radius_charge = 8,
                        subweapons = [STANDARD_GUN])

SHIP_1_MOVEMENT = ShipMovement(8, 30, 0.2)
SHIP_1_SHAPE = ShipShape(40, 30)
SHIP_1 = Ship(1, MACHINE_GUN, SHIP_1_MOVEMENT, SHIP_1_SHAPE)

SHIP_2_MOVEMENT = ShipMovement(5, 30, 0.2)
SHIP_2_SHAPE = ShipShape(40, 30)
SHIP_2 = Ship(2, SNIPER, SHIP_2_MOVEMENT, SHIP_2_SHAPE)

SHIP_3_MOVEMENT = ShipMovement(7, 30, 0.2)
SHIP_3_SHAPE = ShipShape(60, 30)
SHIP_3 = Ship(3, DOUBLE_GUN, SHIP_3_MOVEMENT, SHIP_3_SHAPE)
