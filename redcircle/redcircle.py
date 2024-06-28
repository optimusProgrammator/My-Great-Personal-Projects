"""
This is a program where it finds the center of a red ball in an image and outputs the coordinates
"""
from PIL import Image

def is_red(r, g, b):
    return 150 <= r <= 255 and 0 <= g <= 100 and 0 <= b <= 160

# Load the image
image_path = "redball.jpeg"
image = Image.open(image_path)
image_a = image.load()

# Create an output image to draw to
output = image.copy()

red_circle = []

width, height = image.size

for i in range(width):
    for j in range(height):
        pixel = image_a[i, j]
        red, green, blue = pixel[0], pixel[1], pixel[2]
        
        if is_red(red, green, blue):
            red_circle.append((i, j))
            
if red_circle:
    avg_x = sum(x for x, y in red_circle) // len(red_circle)
    avg_y = sum(y for x, y in red_circle) // len(red_circle)
    center = (avg_x, avg_y)

    print(f"Coordinates are {center}")
    
    # Place a white pixel at the center
    output.putpixel(center, (255, 255, 255))

# Show and save the output image
output.show()
output.save("redball.png", "PNG")
