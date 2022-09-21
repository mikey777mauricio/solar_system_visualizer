# Author: Mikey Mauricio
# Date: Friday, May 7, 2021
# Purpose: System Class

from math import sqrt

G = 6.67384*(10**(-11))  # universal gravitational constant


class System:
    def __init__(self, body_list):
        """sets lists of bodies to body list"""
        self.body_list = body_list

    def compute_acceleration(self, n):
        """computes total x and y components of acceleration"""
        total_ax = 0
        total_ay = 0

        # loop through bodies
        for body in self.body_list:
            if body != n:
                dx = body.x - n.x  # x distance
                dy = body.y - n.y  # y distance
                r = sqrt(dx ** 2 + dy ** 2)  # total distance
                a = G * body.mass / r ** 2  # compute acceleration
                ax = a * dx / r  # compute ax
                ay = a * dy / r  # compute ay
                total_ax += ax  # compute total x acceleration
                total_ay += ay  # compute total y acceleration
        return total_ax, total_ay  # return total ax and ay values

    def update(self, timestep):
        """updates position and velocities of each body in list"""
        for body in self.body_list:
            body.update_position(timestep)  # update each body position
        for body in self.body_list:
            (ax, ay) = self.compute_acceleration(body)  # compute acceleration
            body.update_velocity(ax, ay, timestep)  # update velocities

    def draw(self, cx, cy, pixels_per_meter):
        """draws each body in body list"""
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)  # draw each body
