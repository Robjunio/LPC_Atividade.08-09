import random

def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)
def snake(screen):   
    while True:
        apple_pos = on_grid_random()
        apple = pygame.Surface((10, 10))
        apple.fill((255, 0, 0))
