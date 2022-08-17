import pygame
import sys
from random import randint
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
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
# logic vars
is_fruit_spawned = False
snake_parts = [(0, 0), (0, 0), (0, 0), (GRID_SIZE, 0)]
next_move = pygame.time.get_ticks() + 100
current_direction = 'DOWN'
fruit_pos = None
# FUNCTIONS
def draw_grid():
    for i in range(0, YLINES):
        pygame.draw.line(SCREEN, LINE_COLOR, (0, GRID_SIZE * i), (SCREEN_WIDTH, GRID_SIZE * i))

    for i in range(0, XLINES):
        pygame.draw.line(SCREEN, LINE_COLOR, (GRID_SIZE * i, 0), (GRID_SIZE * i, SCREEN_HEIGHT))
def draw_snake():
    color = (255, 0, 0)
    for index, i in enumerate(snake_parts):
        rect = pygame.Rect(i, (GRID_SIZE, GRID_SIZE))
        if index < len(snake_parts) - 1:
            pygame.draw.rect(SCREEN, color, rect)
        else:
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    move_snake()
def move_snake():
    global snake_parts
    global next_move

    if pygame.time.get_ticks() >= next_move:
        for i in range(0, len(snake_parts)):
            is_last = i == len(snake_parts) - 1
            last_x = snake_parts[-1][0]
            last_y = snake_parts[-1][1]

            if current_direction == 'RIGHT' and is_last:
                snake_parts[i] = (last_x + GRID_SIZE, last_y)
                break
            elif current_direction == 'DOWN' and is_last:
                snake_parts[i] = (last_x, last_y + GRID_SIZE)
                break
            elif current_direction == 'UP' and is_last:
                snake_parts[i] = (last_x, last_y - GRID_SIZE)
                break
            elif current_direction == 'LEFT' and is_last:
                snake_parts[i] = (last_x - GRID_SIZE, last_y)
                break

            snake_parts[i] = snake_parts[i + 1]

        next_move = pygame.time.get_ticks() + 100
def spawn_random_fruit():
    global is_fruit_spawned
    global SCREEN
    global fruit_pos
    if is_fruit_spawned:
        return
    xpos, ypos = randint(0, XLINES - 2) * GRID_SIZE, randint(0, YLINES - 2) * GRID_SIZE
    fruit_pos = (xpos, ypos)
    is_fruit_spawned = True
    print((xpos, ypos))
def draw_fruit():
    global fruit_pos
    global is_fruit_spawned
    global snake_parts
    if not is_fruit_spawned:
        spawn_random_fruit()

    snake_head = snake_parts[-1]

    if snake_head == fruit_pos:
        is_fruit_spawned = False

        snake_parts.insert(0, snake_parts[0])

        fruit_pos = None

    if fruit_pos is None:
        return

    color = (0, 0, 255)
    rect = pygame.Rect(fruit_pos, (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(SCREEN, color, rect)
def handle_events():
    global current_direction
    for e in pygame.event.get():

        # handle quit
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # handle keys
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT and current_direction != 'RIGHT':
                current_direction = 'LEFT'
            if e.key == pygame.K_RIGHT and current_direction != 'LEFT':
                current_direction = 'RIGHT'
            if e.key == pygame.K_UP and current_direction != 'DOWN':
                current_direction = 'UP'
            if e.key == pygame.K_DOWN and current_direction != 'UP':
                current_direction = 'DOWN'
def check_collissions():
    global snake_parts

    snake_head = snake_parts[-1]
    for index, i in enumerate(snake_parts):
        if index == len(snake_parts) - 1:
            break
        if snake_head == i:
            # snake hits its body and dies
            snake_parts = [(0, 0), (0, 0), (0, 0), (GRID_SIZE, 0)]

        # x boundaries
        if snake_head[0] > SCREEN_WIDTH:
            snake_parts[-1] = (0, snake_head[1])
        if snake_head[0] < 0:
            snake_parts[-1] = (SCREEN_WIDTH,snake_head[1])

        # y boundaries
        if snake_head[1] > SCREEN_HEIGHT:
            snake_parts[-1] = (snake_head[0], 0)
        if snake_head[1] < 0:
            snake_parts[-1] = (snake_head[0],SCREEN_HEIGHT)
def mainloop():
    SCREEN.fill((0, 0, 0))
    handle_events()
    draw_snake()
    draw_fruit()
    # draw_grid()
    check_collissions()
    pygame.display.update()
    CLOCK.tick(FPS)
while True:
    mainloop()
