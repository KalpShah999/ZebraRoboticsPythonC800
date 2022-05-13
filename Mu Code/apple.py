import random
import pygame
from config import Config

class Apple():
    def __init__(self):
        self.x = random.randint(5, 64) * 10
        self.y = random.randint(5, 58) * 10

    def NewPosition(self):
        self.x = random.randint(5, 64) * 10
        self.y = random.randint(5, 58) * 10

    def UpdateVisuals(self, display):
        self.appleBody = pygame.draw.rect(display, Config.get("colors").get("apple-red"), (self.x, self.y, 10, 10))
