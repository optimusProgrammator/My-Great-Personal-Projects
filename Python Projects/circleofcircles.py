# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:18:12 2024

@author: 2561986  : Justin Marcel Camonayan

Create a ring of 36 alternating colour circles.
- Each circle should have a radius of 10pixels
- The large circle should have a diameter of 200 pixels
- You should bring the turtle back to the centre of the large circle, turn the turtle 10 degrees  before drawing the next circle.
- Use a list and modulus to alternate between the 3 different colours

"""

import turtle
import math

santiago = turtle.Turtle()
santiago.speed(0)  # Set the turtle speed to the fastest

colors = ["red", "orange", "yellow"]  # List of alternating colors
big_radius = 200  # Radius of the big circle
num_circles = 36  # Number of circles
small_radius = 10  # Radius of the smaller circles

# Draw the big circle
santiago.penup()
santiago.setposition(0, -big_radius)
santiago.pendown()
santiago.circle(big_radius)

# Draw smaller circles around the circumference of the big circle
for i in range(num_circles):
    color = colors[i % len(colors)]  # Alternate between colors using modulus
    angle = i * (360 / num_circles)
    x = big_radius * math.cos(math.radians(angle))
    y = big_radius * math.sin(math.radians(angle))
    
    santiago.penup()
    santiago.goto(x, y)
    santiago.pendown()
    
    santiago.fillcolor(color)
    santiago.begin_fill()
    santiago.circle(small_radius)
    santiago.end_fill()

santiago.penup()
santiago.goto(0, 10)
santiago.stamp()


# Hide turtle and display result
turtle.done()
turtle.bye()
