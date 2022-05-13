import pygame
from config import Config

class Snake():
    def __init__(self):
        self.x = 34
        self.y = 28
        self.direction = "right"
        self.locations = []
        self.increaseSize = False

        self.locations.append([self.x, self.y])

    def IncreaseSize(self):
        self.increaseSize = True

    def Move(self, game):
        if (self.direction == "right"):
            self.x += 1
        elif (self.direction == "left"):
            self.x -= 1
        elif (self.direction == "up"):
            self.y -= 1
        else:
            self.y += 1

        for i in range(len(self.locations)):
            if [self.x, self.y] == self.locations[i]:
                game.gameEnded = True
        if (self.x >= 65 or self.x <= 4 or self.y >= 59 or self.y <= 4):
            game.gameEnded = True

        if (not game.gameEnded):
            if (not self.increaseSize):
                self.locations.pop(0)
            else:
                self.increaseSize = False

            self.locations.append([self.x, self.y])

    def UpdateVisuals(self, display, game):
        for location in self.locations:
            temp = pygame.draw.rect(display, Config.get("colors").get("green"), (location[0] * 10, location[1] * 10, 10, 10))
            if temp.colliderect(game.spawnedApple.appleBody):
                game.spawnedSnake.IncreaseSize()
                game.spawnedApple.NewPosition()
