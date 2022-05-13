import pygame

pygame.init()

pygame.display.set_caption("Hourglass Movement")

screen = pygame.display.set_mode((400, 400))

quitVar = True

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]

image = pygame.image.load("kalp_image.png")
image_x = 0
image_y = 0

hourglassStep = 1

FPS = 60
fpsClock = pygame.time.Clock()

while quitVar == True:

    screen.fill(GREEN)

    screen.blit(image, (image_x, image_y))

    if hourglassStep == 1 or hourglassStep == 3:
        image_x += 1
        if image_x >= 280 and hourglassStep == 1:
            hourglassStep = 2
        elif image_x >= 280 and hourglassStep == 3:
            hourglassStep = 4
    elif hourglassStep == 2:
        image_x -= 1
        image_y += 1
        if image_x <= 0:
            hourglassStep = 3
    elif hourglassStep == 4:
        image_x -= 1
        image_y -= 1
        if image_x <= 0:
            hourglassStep = 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            quitVar = False

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()
