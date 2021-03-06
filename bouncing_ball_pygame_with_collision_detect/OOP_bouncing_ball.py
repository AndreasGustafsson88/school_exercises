import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Ball:
    def __init__(self, x, y, x_step, y_step, color, radius, screen):
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step
        self.color = color
        self.radius = radius
        self.screen = screen
        self.next_x = x
        self.next_y = y

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1
        if not self.radius <= self.y <= SCREEN_HEIGHT - self.radius:
            self.y_step *= -1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(self.screen, self.color, (self.next_hit()), self.radius, 2)

    def next_hit(self):
        self.next_x, self.next_y = self.x, self.y
        while True:
            self.next_x += self.x_step
            self.next_y += self.y_step
            if not self.radius <= self.next_x <= SCREEN_WIDTH - self.radius:
                return self.next_x, self.next_y
            if not self.radius <= self.next_y <= SCREEN_HEIGHT - self.radius:
                return self.next_x, self.next_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    colors = [WHITE, RED, GREEN, BLUE]

    balls = []
    for _ in range(3):
        x = random.randrange(10, SCREEN_WIDTH-10)
        y = random.randrange(10, SCREEN_HEIGHT-10)
        x_step = random.choice([-3, -2, -1, 1, 2, 3])
        y_step = random.choice([-3, -2, -1, 1, 2, 3])
        color = random.choice(colors)
        radius = random.randrange(5, 20)
        ball = Ball(x, y, x_step, y_step, color, radius, screen)
        balls.append(ball)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)

        for ball in balls:
            ball.move()
            ball.next_hit()
            ball.draw()
        pygame.display.update()
        clock.tick(120)

if __name__ == '__main__':
    main()
