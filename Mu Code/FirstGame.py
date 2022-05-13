import pygame

pygame.init()

pygame.display.set_caption("MY FIRST GAME")

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

    screen.fill(WHITE)

    #font = pygame.font.Font("./FirstGameFont.ttf", 20)
    #text = font.render("Hello World", True, GREEN)
    #textRect = text.get_rect(center = (200, 200))
    #screen.blit(text, textRect)

    #pygame.draw.line(screen, GREEN, (200, 180), (200, 220), 4)
    #pygame.draw.rect(screen, GREEN, (100, 100, 50, 50))

    screen.blit(image, (0, 0))

    if hourglassStep == 1:
        image_x += 1


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            quitVar = False

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()
