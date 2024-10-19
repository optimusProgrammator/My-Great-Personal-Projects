import pygame

# Initialize the pygame window
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# player
player_image = pygame.image.load('001-spaceship.png')
playerX = 300
playerY = 350
x_change = 0
y_change = 0

def player(x,y):
    screen.blit(player_image, (x, y))

# Title and Icons
pygame.display.set_caption("Hello World")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


run_time = True
while run_time:

    # RGB = (red, green, blue)
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_time = False

    # If keystroke is pressed, check whether if right or left
        if event.type == pygame.KEYDOWN:
            print("Key is pressed")
            if event.key == pygame.K_LEFT:
                x_change = -0.5
            if event.key == pygame.K_RIGHT:
                x_change = 0.5
            if event.key == pygame.K_UP:
                y_change = -0.5
            if event.key == pygame.K_DOWN:
                y_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    # 5 = 5 + - 0.1 -> 5 - 0.1 = 4.9
    # 5. =5 + 0.1 = 5.1
    playerX += x_change
    playerY += y_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 770:
        playerX = 770
    if playerY <= 0:
        playerY = 0
    elif playerY >= 570:
        playerY = 570
    player(playerX, playerY)
    pygame.display.update()
