import pygame

pygame.init()
pygame.display.set_caption("Game TITLE")
screen = pygame.display.set_mode ( (400,300))

WHITE  = [255, 255, 255]
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255, 0]
BLUE = [0,0,255]

quitvar = True

while quitvar == True:
    screen.fill (WHITE)
    pygame.draw.polygon(screen, GREEN, ((200,140), (190,150), (194,162), (206,162), (210,150)))
    pygame.draw.line(screen, RED, (0,0), (60,0),4)
    pygame.draw.line(screen, BLACK, (60,0), (0,60),4)
    pygame.draw.line(screen, GREEN, (0,60), (60,60),4)
    pygame.draw.circle(screen, RED, (380,20), 20, 0)
    pygame.draw.ellipse(screen,BLACK, (360,292, 40, 8), 1)
    pygame.draw.rect(screen, BLUE, (0,250,100,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitvar = False

    pygame.display.update()

pygame.quit()
