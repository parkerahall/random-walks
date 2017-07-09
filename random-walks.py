#!/usr/bin/env python

"""
Script takes five arguments in call:
    .random-walks.py min_turns max_turns length speed file
"""

import sys
import turtle
import random

# represent directions to move as (x,y) tuples
FORWARD = (0, 1)
BACK = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)

DIRECTION_LIST = [FORWARD, BACK, RIGHT, LEFT]

"""
no input
output: (x, y) tuple representing a randomly
        selected direction
"""
def pick_direction():
    return random.choice(DIRECTION_LIST)

"""
input: length, size of steps to take
        bound, upper bound of steps to take
        file, string filepath to write resulting picture to
output: num_turns, total number of turns taken
"""
def draw(length, bound, file):
    current_x = 0
    current_y = 0
    num_turns = 0
    turtle.left(90)
    
    while ((current_x != 0 or current_y != 0 or num_turns == 0) and num_turns < bound):
        delta_x, delta_y = pick_direction()
        new_x = current_x + delta_x * length
        new_y = current_y + delta_y * length
        turtle.goto(new_x, new_y)

        current_x, current_y = new_x, new_y
        num_turns += 1

    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=file)
    return num_turns

"""
creates random walk pattern and saves it to file specified by user
user determines speed, size, lower bound and upper bound for walk as well
walk will restart if home is reached before lower bound
walk will end if upper bound is reached
"""
if __name__ == "__main__":
        try:
            lower_bound = int(sys.argv[1])
            upper_bound = int(sys.argv[2])
            length = int(sys.argv[3])
            speed = int(sys.argv[4])
            filename = sys.argv[5]
        except IndexError:
            print("Call to script not formatted correctly.")
            print("./random-walks.py [LOWER BOUND] [UPPER BOUND] [LENGTH] [SPEED] [FILE]")
            sys.exit()

        turtle.speed(speed)
        num_turns = lower_bound - 1
        while num_turns < lower_bound:
            turtle.reset()
            num_turns = draw(length, upper_bound, filename)
        turtle.done()