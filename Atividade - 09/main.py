import pygame
from Snake import *
from Cube import *
from Bot import *
from utils import *

if __name__ == "__main__":
    snake = Snake(SNAKE_COLOR, SNAKE_STARTING_POSITION)
    pygame.init()
    clock = pygame.time.Clock()

    running = True

    while running:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        # TODO inserir comando pra desenhar os elementos da tela

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
