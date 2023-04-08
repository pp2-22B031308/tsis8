import collections
import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError


class Button(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 - self.size // 2,
                20,
                self.size,
                self.size,
            ),
        )


class Pen(GameObject):
    def __init__(self):
        self.points = []

    def draw(self):
        for i in range(len(self.points) - 1):
            start_pos = self.points[i]
            end_pos = self.points[i + 1]
            pygame.draw.line(SCREEN, WHITE, start_pos, end_pos, 5)

    def update(self, current_pos):
        self.points.append(current_pos)


def main():
    running = True
    active_obj = None

    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                active_obj = Pen()

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.update(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                active_obj.draw()
                active_obj = None

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
