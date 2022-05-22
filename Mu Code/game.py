import pygame
from snake import Snake
from apple import Apple
from config import Config

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((700, 700))
        self.time = 0
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        self.spawnedApple = Apple()
        self.spawnedSnake = Snake()
        self.gameEnded = False
        self.quitVar = True
        while (self.quitVar):
            if (not self.gameEnded):
                self.loop()
            else:
                self.gameOver()

    def loop(self):
        self.screen.fill(Config.get("colors").get("black"))

        font = pygame.font.Font("./FirstGameFont.ttf", 20)
        text = font.render("Score: " + (str)(len(self.spawnedSnake.locations) - 1), True, (255, 255, 255))
        textRect = text.get_rect(center = (350, 650))
        self.screen.blit(text, textRect)

        self.border1 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (40, 40, 620, 10))
        self.border2 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (40, 50, 10, 540))
        self.border3 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (650, 50, 10, 540))
        self.border4 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (40, 590, 620, 10))

        self.spawnedApple.UpdateVisuals(self.screen)

        if (self.time % 5 == 0):
            self.spawnedSnake.Move(self)

        self.spawnedSnake.UpdateVisuals(self.screen, self)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitVar = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spawnedApple.NewPosition()
                if event.key == pygame.K_UP and self.spawnedSnake.direction != "down":
                    self.spawnedSnake.direction = "up"
                if event.key == pygame.K_DOWN and self.spawnedSnake.direction != "up":
                    self.spawnedSnake.direction = "down"
                if event.key == pygame.K_RIGHT and self.spawnedSnake.direction != "left":
                    self.spawnedSnake.direction = "right"
                if event.key == pygame.K_LEFT and self.spawnedSnake.direction != "right":
                    self.spawnedSnake.direction = "left"

        pygame.display.update()
        self.time += 1

        self.fpsClock.tick(self.FPS)

    def gameOver(self):
        self.screen.fill(Config.get("colors").get("black"))

        font = pygame.font.Font("./FirstGameFont.ttf", 20)
        text = font.render("Score: " + (str)(len(self.spawnedSnake.locations)), True, (255, 255, 255))
        textRect = text.get_rect(center = (350, 650))
        self.screen.blit(text, textRect)

        self.border1 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (40, 40, 620, 10))
        self.border2 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (40, 50, 10, 540))
        self.border3 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (650, 50, 10, 540))
        self.border4 = pygame.draw.rect(self.screen, Config.get("colors").get("white"), (40, 590, 620, 10))

        self.spawnedApple.UpdateVisuals(self.screen)

        self.spawnedSnake.UpdateVisuals(self.screen, self)

        font2 = pygame.font.Font("./FirstGameFont.ttf", 50)
        text2 = font2.render("Game Over!", True, Config.get("colors").get("white"))
        textRect2 = text2.get_rect(center = (350, 350))
        self.screen.blit(text2, textRect2)

        font3 = pygame.font.Font("./FirstGameFont.ttf", 20)
        text3 = font3.render("Press 'Space' to play again, press 'c' to exit", True, Config.get("colors").get("white"))
        textRect3 = text3.get_rect(center = (350, 400))
        self.screen.blit(text3, textRect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitVar = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gameEnded = False
                    self.time = 0
                    self.spawnedApple = Apple()
                    self.spawnedSnake = Snake()
                if event.key == pygame.K_c:
                    self.quitVar = False
                    pygame.quit()

        pygame.display.update()

        self.fpsClock.tick(self.FPS)
