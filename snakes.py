import pygame
import random

# Set up constants
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
FPS = 10

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 25)

# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH/2, HEIGHT/2)]
        self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    def collide(self):
        x, y = self.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True
        for bx, by in self.body[1:]:
            if x == bx and y == by:
                return True
        return False

    def eat(self, food):
        x, y = self.body[0]
        fx, fy = food
        if x == fx and y == fy:
            self.body.append(food)
            return True
        return False

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH-CELL_SIZE)
        self.y = random.randint(0, HEIGHT-CELL_SIZE)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, CELL_SIZE, CELL_SIZE))

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    # Move the Snake
    snake.move()

    # Check for collisions
    if snake.collide():
        running = False

    # Check for food
    if snake.eat((food.x, food.y)):
        food = Food()

    # Draw the Snake and Food
    screen.fill(BLACK)
    snake.draw()
    food.draw()

    # Update the screen
    pygame.display.update()

    # Wait for the next frame
    clock.tick(FPS)

# Game over screen
text = font.render("Game Over", True, WHITE)
text_rect = text.get
