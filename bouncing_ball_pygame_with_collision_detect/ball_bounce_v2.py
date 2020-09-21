import pygame
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 120


def collide(x, y, x_step, y_step):
    while True:
        x += x_step
        y += y_step
        if x >= 790 or x <= 10:
            return x, y
        if y >= 590 or y <= 10:
            return x, y

def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    next_x = -50
    next_y = -50
    y = 300
    y_step = 2
    x = 400
    x_step = 2
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)

        y += y_step
        if y >= 590 or y <= 10:
            y_step *= -1
            next_x, next_y = collide(x, y, x_step, y_step)
        x += x_step
        if x >= 790 or x <= 10:
            x_step *= -1
            next_x, next_y = collide(x, y, x_step, y_step)

        pygame.draw.circle(screen, BLUE, (next_x, next_y), 10, 2)
        pygame.draw.circle(screen, RED, (x, y), 10)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
