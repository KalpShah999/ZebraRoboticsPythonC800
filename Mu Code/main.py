import pygame
from snake import Snake
from apple import Apple
from config import Config
from game import Game


snakeGame = Game()

while snakeGame.quitVar:
    if (not snakeGame.gameEnded):
        snakeGame.loop()
    else:
        snakeGame.gameOver()

pygame.quit()
