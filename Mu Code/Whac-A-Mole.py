import pygame
import random

pygame.init()

pygame.display.set_caption("Whac-A-Kalp")

screen = pygame.display.set_mode((700, 700))

quitVar = True

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]

score = 0

FPS = 60
fpsClock = pygame.time.Clock()
time = 0

image = pygame.image.load("kalp_image.png")
image_x = random.randint(0, 580)
image_y = random.randint(50, 580)

position = [1000, 1000]

while quitVar == True:

    screen.fill(WHITE)

    font = pygame.font.Font("./FirstGameFont.ttf", 20)
    text = font.render("Score: " + (str)(score), True, GREEN)
    textRect = text.get_rect(center = (50, 10))
    screen.blit(text, textRect)

    screen.blit(image, (image_x, image_y))

    if time % FPS * 1.5 == 0:
        time = 0
        image_x = random.randint(0, 580)
        image_y = random.randint(50, 580)

    if abs(position[0] - (image_x + 60)) <= 60 and abs(position[1] - (image_y + 60)) <= 60:
        time = 0
        score += 1
        image_x = random.randint(0, 580)
        image_y = random.randint(50, 580)
        position = [1000, 1000]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

    pygame.display.update()

    time += 1
    fpsClock.tick(FPS)

pygame.quit()
