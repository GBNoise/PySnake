import pygame
import sys
from Snake import Snake
from Fruit import Fruit

# PYGAME INITIALIZATION
pygame.init()
# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 450
FPS = 60
GRID_SIZE = 30
LINE_COLOR = (255, 255, 255)
YLINES = int(SCREEN_HEIGHT / GRID_SIZE) + 1
XLINES = int(SCREEN_WIDTH / GRID_SIZE) + 1
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
snake = Snake(size=GRID_SIZE, SCREEN=SCREEN, xboundary=SCREEN_WIDTH, yboundary=SCREEN_HEIGHT)
fruit = Fruit(snake=snake, screen=SCREEN, size=GRID_SIZE, xlines=XLINES, ylines=YLINES)


# FUNCTIONS
def draw_grid():
    for i in range(0, YLINES):
        pygame.draw.line(SCREEN, LINE_COLOR, (0, GRID_SIZE * i), (SCREEN_WIDTH, GRID_SIZE * i))

    for i in range(0, XLINES):
        pygame.draw.line(SCREEN, LINE_COLOR, (GRID_SIZE * i, 0), (GRID_SIZE * i, SCREEN_HEIGHT))


def handle_events():
    global current_direction
    for e in pygame.event.get():

        # handle quit
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # handle keys
        snake.handle_movement(e)


def mainloop():
    SCREEN.fill((0, 0, 0))
    handle_events()
    snake.draw_snake()
    fruit.draw_fruit()
    # draw_grid()
    snake.check_collissions()
    pygame.display.update()
    CLOCK.tick(FPS)


while 69 == 69:
    mainloop()
