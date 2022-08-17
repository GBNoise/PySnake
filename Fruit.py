import pygame
from random import randint

class Fruit:
    def __init__(self,snake = None, screen = None, size = 30, xlines = None, ylines = None, hud=None):
        if not snake or not screen or not xlines or not ylines or not hud:
            raise ValueError('props cannot be null')

        self.snake = snake
        self.SCREEN = screen
        self.GRID_SIZE = size
        self.XLINES = xlines
        self.YLINES = ylines
        self.is_fruit_spawned = False
        self.fruit_pos = None
        self.hud = hud


    def draw_fruit(self):
        if not self.is_fruit_spawned:
            self.spawn_random_fruit()

        snake_head = self.snake.snake_parts[-1]

        if snake_head == self.fruit_pos:
            self.is_fruit_spawned = False
            self.snake.snake_parts.insert(0, self.snake.snake_parts[0])
            self.fruit_pos = None
            self.snake.fruits_eaten += 1
            self.hud.score = self.snake.fruits_eaten
            self.hud.update_score()

        if self.fruit_pos is None:
            return

        color = (0, 0, 255)
        rect = pygame.Rect(self.fruit_pos, (self.GRID_SIZE, self.GRID_SIZE))
        pygame.draw.rect(self.SCREEN, color, rect)

    def spawn_random_fruit(self):
        if self.is_fruit_spawned:
            return
        xpos, ypos = randint(0, self.XLINES - 2) * self.GRID_SIZE, randint(0, self.YLINES - 2) * self.GRID_SIZE
        self.fruit_pos = (xpos, ypos)
        self.is_fruit_spawned = True
