# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:05:03 2024

@author: 2561986

These are simples exercises of coding nested loops
"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = "")
    print("")
 
print("____________________\n")
 
for i in range(5, 0, -1): 
    print(" " * (5 - i), end="")  
    print("*" * i) 
 
print("____________________\n")
 
for i in range(10, 21):
    print(f"Factors of {i}: ", end="")
    for factor in range(1, i + 1):
        if i % factor == 0:
            print(f"{factor},", end=" ")
    print() 
    
import turtle

# Create turtle object
santiago = turtle.Turtle()
santiago.speed(0)

# Set starting position
santiago.penup()
santiago.goto(-250, 250)
santiago.pendown()

# Define colors
colors = ["black", "red"]

# Draw the checkerboard
for column in range(10):
    for row in range(10):
        santiago.fillcolor(colors[(column+row) % 2])
        santiago.begin_fill()
        for _ in range(4):
            santiago.forward(50)
            santiago.right(90)
        santiago.end_fill()
        santiago.forward(50)
    santiago.penup()
    santiago.goto(-250, santiago.ycor() - 50)
    santiago.pendown()

# Hide the turtle
santiago.hideturtle()

# Keep the window open
turtle.done()

