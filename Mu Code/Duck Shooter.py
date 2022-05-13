import pygame
import random

pygame.init()

pygame.display.set_caption("Kalp Shooter")

screen = pygame.display.set_mode((700, 700))

quitVar = True

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
BLUE = [0, 130, 255]

score = 0
shots = 0

FPS = 60
fpsClock = pygame.time.Clock()
time = 0

position = [1000, 1000]

birds = []


class Bird:
    def __init__(self):
        self.speed = random.randint(1, 7)
        self.isRight = random.randint(0, 1)
        if (self.isRight == 1):
            self.x = random.randint(0, 100) + 480
        else:
            self.x = random.randint(0, 100)
        self.y = random.randint(200, 580)

        self.image = pygame.image.load("kalp_image.png")

        screen.blit(self.image, (self.x, self.y))


while quitVar == True:

    screen.fill(BLUE)

    font = pygame.font.Font("./FirstGameFont.ttf", 20)
    text = font.render("Score: " + (str)(score) + ", Shots: " + (str)(shots), True, GREEN)
    textRect = text.get_rect(center = (350, 650))
    screen.blit(text, textRect)

    for bird in birds:
        screen.blit(bird.image, (bird.x, bird.y))

        bird.y -= bird.speed
        if (bird.isRight == 1):
            bird.x -= bird.speed
        else:
            bird.x += bird.speed

        if abs(position[0] - (bird.x + 60)) <= 60 and abs(position[1] - (bird.y + 60)) <= 60:
            score += 1
            birds.remove(bird)
            position = [1000, 1000]
        elif bird.y < -120:
            birds.remove(bird)

    position = [1000, 1000]

    if time % 60 == 0 and time < 550:
        birds.append(Bird())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            shots += 1

    if time < 600:
        time += 1
    else:
        birds.clear()
        font2 = pygame.font.Font("./FirstGameFont.ttf", 100)
        text2 = font2.render("Time's Up!", True, GREEN)
        textRect2 = text2.get_rect(center = (350, 350))
        screen.blit(text2, textRect2)

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit()
