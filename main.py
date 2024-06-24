import pygame
import random

pygame.init()
pygame.display.set_caption("snake")

positions = []
direction = [False, False, True, False]

width = 400
height = 400

length = 1

fx = random.randint(0, width - 10)
fy = random.randint(0, height - 10)

x = width / 2
y = height / 2
cwidth = 10
cheight = 10
velocity = 10

run = True
while run:
    pygame.time.delay(100)

    win = pygame.display.set_mode((width, height))
    win.fill((0, 128, 0))
    pygame.draw.rect(win, (255, 255, 0), (x, y, cwidth, cheight))

    positions.append((x, y, cwidth, cheight))
    if not len(positions) <= length:
        positions.pop(0)

    for r in positions:
        pygame.draw.rect(win, (255, 255, 0), r)

    pygame.draw.rect(win, (128, 0, 0), (fx, fy, 10, 10))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and not direction[2]:
        direction = [False, False, False, True]

    if keys[pygame.K_RIGHT] and not direction[3]:
        direction = [False, False, True, False]

    if keys[pygame.K_UP] and not direction[1]:
        direction = [True, False, False, False]

    if keys[pygame.K_DOWN] and not direction[0]:
        direction = [False, True, False, False]

    if direction[0]:
        y -= velocity
    if direction[1]:
        y += velocity
    if direction[3]:
        x -= velocity
    if direction[2]:
        x += velocity

    if abs(x - fx) <= 10 and abs(y - fy) <= 10:
        fx = random.randint(0, width - 10)
        fy = random.randint(0, height - 10)
        length += 1

    if x < 0 or y < 0 or x + 10 > width or y + 10 > width:
        run = False

    for r in positions:
        x1 = r[0]
        y1 = r[1]
        if abs(x - x1) < 10 and abs(y - y1) < 10:
            run = False
