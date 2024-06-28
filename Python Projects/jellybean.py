# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:49:43 2024

@author: 2561986

JELLYBEAN PROGRAM

Description:
    
    - Import image processing libraries
    - Define a color function 
    - Load image of jellybeans
    - Create a list to store the pixels for each color
    - Go through all pixels in the image
    - If it's a known color, add that pixel to the respective color list
    - Get the length of each color pixel list (same as the number of color pixels)
    - Calculate the percentage of each color pixels over the total number of pixels in the image
    - Output a report
"""

from PIL import Image

# A function that returns the color of the r, g, b values
def colour(r, g, b):
    if 0 <= r < 25 and 230 < g == 255 and 0 <= b < 25:
        return "green"
    elif 255 > 230 < r and 0 <= g < 25 and 0 <= b < 25:
        return "red"
    elif 0 <= r < 25 and 0 <= g < 25 and 230 < b == 255:
        return "blue"
    elif r == 255 and g == 255 and b == 255:
        return "white"
    elif r == 0 and g == 0 and b == 0:
        return "black"
    elif 255 > 230 < r and 255 > 230 < g and b == 0:
        return "yellow"
    elif 255 > 230 < r and g == 0 and 0 <= g < 25 and 230 < b == 255:
        return "magenta"
    else:
        return "None"

# Initialize lists to store pixels of each color
green_pixels = []
red_pixels = []
blue_pixels = []
yellow_pixels = []

# Open the image file
image = Image.open("jelly_beans.jpg")
pixels = image.load()

width, height = image.size
total_pixels = width * height

# Go through every pixel in the image
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j][:3]
        pixel_colour = colour(r, g, b)
        
        if pixel_colour == "green":
            green_pixels.append((i, j))
        elif pixel_colour == "red":
            red_pixels.append((i, j))
        elif pixel_colour == "blue":
            blue_pixels.append((i, j))
        elif pixel_colour == "yellow":
            yellow_pixels.append((i, j))

# Calculate the percentage of each color
green_percentage = (len(green_pixels) / total_pixels) * 100
red_percentage = (len(red_pixels) / total_pixels) * 100
blue_percentage = (len(blue_pixels) / total_pixels) * 100
yellow_percentage = (len(yellow_pixels) / total_pixels) * 100

# Output the report
print("Color Report:")
print(f"Green: {len(green_pixels)} pixels ({green_percentage:.2f}%)")
print(f"Red: {len(red_pixels)} pixels ({red_percentage:.2f}%)")
print(f"Blue: {len(blue_pixels)} pixels ({blue_percentage:.2f}%)")
print(f"Yellow: {len(yellow_pixels)} pixels ({yellow_percentage:.2f}%)")

# Save the output image
image.save("output.png", "PNG")
