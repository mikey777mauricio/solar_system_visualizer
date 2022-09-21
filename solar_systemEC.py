# Author: Mikey Mauricio
# Date: Friday, May 7, 2021
# Purpose: System and Body Driver

from cs1lib import *
from system import System
from bodyEC import Body
from random import randint
from stars import Stars

WINDOW_WIDTH = 1100  # window height
WINDOW_HEIGHT = 800 # window width

TIME_SCALE = 200000         # real seconds per simulation second
PIXELS_PER_METER = 1.7 / 1e9  # distance scale for the simulation

FRAMERATE = 40              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


star_list = []  # list of starts
# loop to create stars
for i in range(int(WINDOW_WIDTH / 2)):
    star_x = randint(0, WINDOW_WIDTH)
    star_y = randint(0, WINDOW_WIDTH)
    single_star = Stars(star_x, star_y)
    star_list.append(single_star)  # add object to list

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # draw stars
    for star in star_list:
        star.draw()


    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, 'sun.png')  # sun-body object
mercury = Body(3.30e23, 5.79e10, 0, 0, 47400, 'mercury.png')  # mercury-body object
venus = Body(4.87e24, 1.082e11, 0, 0, 35000, 'venus.png')  # venus-body object
earth = Body(5.9736e24, 1.496e11, 0, 0, 29800, 'earth.png')  # earth-body object
mars = Body(6.42e23, 2.279e11, 0, 0, 24100, 'mars.png')  # mars-body object

solar_system = System([sun, mercury, venus, earth, mars])  # solar system-system object

start_graphics(main, 2400, framerate=FRAMERATE, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)