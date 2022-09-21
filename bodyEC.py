# Author: Mikey Mauricio
# Date: Friday, May 7, 2021
# Purpose: System Class

from cs1lib import*

class Body:
    def __init__(self, mass, x, y, vx, vy, image):
        """initializes variables for body object"""
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = load_image(image)

    def update_position(self, timestep):
        """updates x and y positions"""
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        """updates velocity of body"""
        self.vx += ax * timestep
        self.vy += ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        """draws body using center x and center y"""
        draw_image(self.image, cx - (self.x * pixels_per_meter), cy - (self.y * pixels_per_meter))
