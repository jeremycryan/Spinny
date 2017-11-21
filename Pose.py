#!/usr/bin/env python

def Pose():
    def __init__(self, position=(0,0), velocity=(0,0), direction=(0,0), spin_speed=0):
        """ Position vector in world frame in pixels
            Velocity vector in world frame in pixels/second
            Direction unit vector in world frame
            Angular velocity in radians/second """
        self.pos = np.asarray(pos)
        self.vel = np.asarray(velocity)
        self.direction = np.asarray(direction)
        self.spin_speed = spin_speed

    def getPose(self, **args):
        """ Constructs a new pose with any unspecified parameters
        copied from this pose. """
        for key, val in vars(self).items():
            if not key in args:
                args[key] = val
        return Pose(**args)

    def update(self, dt):
        """ Updates position and direction by a given timestep. """
        self.translate(self.vel*dt)
        self.rotate(self.spin_speed*dt)

    def translate(self, displacement):
        """ Translates the pose in the global frame. """
        self.pos += displacement

    def rotate(self, angle):
        """ Rotates the pose counterclockwise by an angle in radians. """
        rot_mat = np.asarray([[math.cos(amt), -math.sin(amt)],
                            [math.sin(amt), math.cos(amt)]])
        new_direction = rot_mat.dot(self.direction)
        self.direction = new_direction/np.norm(new_direction)
