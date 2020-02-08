"""
automated drawing script for organizing complex geometrics 
(through examples octogons and line segment constructs), into perfect circles

"""

from turtle import *
from random import *


def octogon(size):
    left(90)
    forward(size / 2)
    right(45)
    for i in range(7):
        forward(size)
        right(45)
    forward(size / 2)
    right(90)
    
def construct_branch(length, min_angle, max_angle):
    forward(length)
    backward(length / 3)
    left(max_angle)
    forward(length / 3)
    octogon(length / 15)
    backward(length / 3)
    right(max_angle * 2)
    forward(length / 3)
    octogon(length / 15)
    backward(length / 3)
    left(max_angle)
    backward(2 * (length / 3))

def construct(length, min_angle, max_angle):
    forward(length)
    left(min_angle)
    construct_branch(length, min_angle, max_angle)
    right(min_angle * 2)
    construct_branch(length, min_angle, max_angle)
    left(min_angle)
    backward(length)

# properties and constraints
pensize(0.3)
diameter = randint(20, 100)
colors = ["grey", "coral", "teal"]
complexity = 2 # additional layers

# initial generator values
color(choice(colors))
turn = randint(3, 90) + random()
angle1 = randint(1, 180)
angle2 = randint(1, 180)
branches = 0
full_circle = 0

# the loop runs any angle set which can be drawn as a perfect circle,
# layering the image with a newly generated patterns by a factor of
# "complexity"

while full_circle <= complexity:
    if full_circle > complexity:
        break
    elif 360 % turn == 0:
        construct(diameter, angle1, angle2)
        left(turn)
        branches = branches + 1
        if turn * branches == 360:
            diameter = randint(20, 100)
            turn = randint(1, 90)
            color(choice(colors))
            angle1 = randint(1, 180)
            angle2 = randint(1, 180)
            branches = 0
            full_circle = full_circle + 1
    else:
        turn = randint(3, 90)
        
# moves the turtle off-screen after drawing.
penup()
forward(5000)
