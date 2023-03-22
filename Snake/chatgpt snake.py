import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the dimensions of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Set the size of the snake and the food
BLOCK_SIZE = 10

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the caption of the window
pygame.display.set_caption("Snake")

# Create a clock to control the frame rate of the game
clock = pygame.time.Clock()

# Define the font for the score
font = pygame.font.Font(None, 36)

# Define the direction constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Define the colors of the snake and the food
snake_color = GREEN
food_color = RED

# Define the initial direction of the snake
direction = RIGHT

# Define the initial position of the snake
snake_pos = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]

# Define the initial position of the food
food_pos = (random.randint(0, SCREEN_WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE, random.randint(0, SCREEN_HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)

# Define the initial score
score = 0

# Define the main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
    
    # Update the snake position
    head_pos = snake_pos[-1]
    if direction == UP:
        new_pos = (head_pos[0], head_pos[1] - BLOCK_SIZE)
    elif direction == DOWN:
        new_pos = (head_pos[0], head_pos[1] + BLOCK_SIZE)
    elif direction == LEFT:
        new_pos = (head_pos[0] - BLOCK_SIZE, head_pos[1])
    elif direction == RIGHT:
        new_pos = (head_pos[0] + BLOCK_SIZE, head_pos[1])
    
    # Check if the snake hits the wall
    if new_pos[0] < 0 or new_pos[0] >= SCREEN_WIDTH or new_pos[1] < 0 or new_pos[1] >= SCREEN_HEIGHT:
        pygame.quit()
        quit()
    
    # Check if the snake hits itself
    if new_pos in snake_pos:
        pygame.quit()
        quit()
    
    # Check if the snake eats the food
    if new_pos == food_pos:
        snake_pos.append(food_pos)
        food_pos = (random.randint(0, SCREEN_WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE, random.randint(0, SCREEN_HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)
        score += 10
    else:
        snake_pos.pop(0)
        snake_pos.append(new_pos)
    
    # Draw the background
    screen.fill(BLACK)
