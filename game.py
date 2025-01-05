import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
SPEED = 20
BLOCK_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.apple = self.generate_apple()
        self.score = 0

    def generate_apple(self):
        while True:
            x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def draw(self):
        win.fill(BLACK)
        for x, y in self.snake:
            pygame.draw.rect(win, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(win, WHITE, (*self.apple, BLOCK_SIZE, BLOCK_SIZE))
        text = font.render(f'Score: {self.score}', True, WHITE)
        win.blit(text, (10, 10))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.direction = 'RIGHT'

        head_x, head_y = self.snake[-1]
        if self.direction == 'UP':
            new_head = (head_x, head_y - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + BLOCK_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head_x - BLOCK_SIZE, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + BLOCK_SIZE, head_y)

        if new_head in self.snake or new_head[0] < 0 or new_head[1] >= HEIGHT:
            pygame.quit()
            sys.exit()

        self.snake.append(new_head)
        if new_head == self.apple:
            self.score += 1
            self.apple = self.generate_apple()
        else:
            self.snake.pop(0)

    def run(self):
        while True:
            self.update()
            self.draw()
            pygame.display.update()
            clock.tick(SPEED)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()