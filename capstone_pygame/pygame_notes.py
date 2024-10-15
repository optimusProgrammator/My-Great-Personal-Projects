import pygame

# Initialize the pygame window
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

run_time = True
while run_time:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_time = False

