import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
chose = True
dt = 0
player_pos = pygame.Vector2(50,50 )
player_pos1 = pygame.Vector2(screen.get_width() -50, screen.get_height() -50)

t = random.randint(1,2)


while running:
    # turn mechanics
    c = random.randint(1,100)
    if c == 53:
        t = random.randint(1, 2)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if t == 1:
        color = "red"
        color1 = "blue"
        a = 1
    elif t == 2:
        color1 = "red"
        color = "blue"
        a = 2

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    keys = pygame.key.get_pressed()
    pygame.draw.circle(screen, color, player_pos, 50)
    pygame.draw.circle(screen, color1, player_pos1, 50)
    # player 1 config
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if player_pos.x > 1230:
        player_pos.x = 1230
    if player_pos.y > 720-50:
        player_pos.y = 720-50
    if player_pos.x < 50:
        player_pos.x = 50
    if player_pos.y < 50:
        player_pos.y = 50
    # player 2 config
    if keys[pygame.K_i]:
        player_pos1.y -= 300 * dt
    if keys[pygame.K_k]:
        player_pos1.y += 300 * dt
    if keys[pygame.K_j]:
        player_pos1.x -= 300 * dt
    if keys[pygame.K_l]:
        player_pos1.x += 300 * dt
    if player_pos1.x > 1230:
        player_pos1.x = 1230
    if player_pos1.y > 720-50:
        player_pos1.y = 720-50
    if player_pos1.x < 50:
        player_pos1.x = 50
    if player_pos1.y < 50:
        player_pos1.y = 50
    if player_pos1.x-50 < player_pos.x < player_pos1.x+50 and player_pos1.y-50 < player_pos.y < player_pos1.y+50:
        if a == 1:
            w = 1
            running = False
        elif a == 2:
            running = False
            w = 2


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
font = pygame.font.Font('freesansbold.ttf', 32)
if w == 1:
    text = "PLAYER 1 WON"
if w == 2:
    text = "PLAYER 2 WOn"
print(text)

pygame.quit()
