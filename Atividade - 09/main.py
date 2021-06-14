import random

from Bot import *
from utils import *


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


if __name__ == "__main__":
    snake = Snake(SNAKE_COLOR, SNAKE_STARTING_POSITION, rows=20, width=WIDTH)
    pygame.init()
    clock = pygame.time.Clock()

    snack = Cube(randomSnack(20, snake), color=RED, rows=20, width=WIDTH)
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while running:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.add_body()
            snack = Cube(randomSnack(20, snake), color=RED, rows=20, width=WIDTH)

        screen.fill((0, 0, 0))
        snake.draw(screen)
        snack.draw(screen)
        pygame.display.update()
