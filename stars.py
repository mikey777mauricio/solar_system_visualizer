from random import randint
from cs1lib import*
class Stars:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1.2

    def draw(self):
        set_fill_color(1, 1, 1)
        draw_circle(self.x, self.y, self.radius)