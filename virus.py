"""
Using turtle to draw corona virus in python
"""

from turtle import *

#Select color and background color
color('green')
bgcolor('black')
#Select speed of motion of turtle and hide it
speed(11)
hideturtle()
#Set the position you want. This works best for me
goto(25, 152)
#Use looping for shape
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1
done()
