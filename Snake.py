import pygame


class Snake:
    def __init__(self, initial_parts=4, size=30, SCREEN=None, xboundary=None, yboundary=None):
        if not SCREEN or not xboundary or not yboundary:
            raise ValueError("properties cannot be null")

        self.snake_parts = [(size, 0)]
        for i in range(1, initial_parts):
            self.snake_parts.insert(0, (0, 0))

        self.next_move = pygame.time.get_ticks() + 100
        self.current_direction = 'DOWN'
        self.SCREEN = SCREEN
        self.GRID_SIZE = size
        self.xboundary = xboundary
        self.yboundary = yboundary
        self.fruits_eaten = 0

    def draw_snake(self):
        color = (255, 0, 0)
        for index, i in enumerate(self.snake_parts):
            rect = pygame.Rect(i, (self.GRID_SIZE, self.GRID_SIZE))
            if index < len(self.snake_parts) - 1:
                pygame.draw.rect(self.SCREEN, color, rect)
            else:
                pygame.draw.rect(self.SCREEN, (0, 255, 0), rect)

        self.move_snake()

    def move_snake(self):
        if pygame.time.get_ticks() >= self.next_move:
            for i in range(0, len(self.snake_parts)):
                is_last = i == len(self.snake_parts) - 1
                last_x = self.snake_parts[-1][0]
                last_y = self.snake_parts[-1][1]

                if self.current_direction == 'RIGHT' and is_last:
                    self.snake_parts[i] = (last_x + self.GRID_SIZE, last_y)
                    break
                elif self.current_direction == 'DOWN' and is_last:
                    self.snake_parts[i] = (last_x, last_y + self.GRID_SIZE)
                    break
                elif self.current_direction == 'UP' and is_last:
                    self.snake_parts[i] = (last_x, last_y - self.GRID_SIZE)
                    break
                elif self.current_direction == 'LEFT' and is_last:
                    self.snake_parts[i] = (last_x - self.GRID_SIZE, last_y)
                    break

                self.snake_parts[i] = self.snake_parts[i + 1]

            self.next_move = pygame.time.get_ticks() + 100

    def check_collissions(self):
        snake_head = self.snake_parts[-1]
        for index, i in enumerate(self.snake_parts):
            if index == len(self.snake_parts) - 1:
                break
            if snake_head == i:
                # snake hits its body and dies
                self.fruits_eaten = 0
                self.snake_parts = [(0, 0), (0, 0), (0, 0), (self.GRID_SIZE, 0)]

            # x boundaries
            if snake_head[0] > self.xboundary:
                self.snake_parts[-1] = (0, snake_head[1])
            if snake_head[0] < 0:
                self.snake_parts[-1] = (self.xboundary, snake_head[1])

            # y boundaries
            if snake_head[1] > self.yboundary:
                self.snake_parts[-1] = (snake_head[0], 0)
            if snake_head[1] < 0:
                self.snake_parts[-1] = (snake_head[0], self.yboundary)

    def handle_movement(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT and self.current_direction != 'RIGHT':
                self.current_direction = 'LEFT'
            if e.key == pygame.K_RIGHT and self.current_direction != 'LEFT':
                self.current_direction = 'RIGHT'
            if e.key == pygame.K_UP and self.current_direction != 'DOWN':
                self.current_direction = 'UP'
            if e.key == pygame.K_DOWN and self.current_direction != 'UP':
                self.current_direction = 'DOWN'
