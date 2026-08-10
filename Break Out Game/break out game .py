import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window with specified dimensions
pygame.display.set_caption(".: Breakout Game :.")  # Set the window title

# Colors for different game elements
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]  # List of colors to be used for bricks

# Paddle settings
paddle_width, paddle_height = 120, 15  # Paddle dimensions
paddle_x = (WIDTH - paddle_width) // 2  # Set the initial horizontal position of the paddle
paddle_y = HEIGHT - 40  # Set the vertical position of the paddle near the bottom
paddle_speed = 12  # Speed of paddle movement

# Ball settings
ball_radius = 10  # Ball radius
ball_x = WIDTH // 2  # Set the initial horizontal position of the ball at the center
ball_y = HEIGHT // 2  # Set the initial vertical position of the ball at the center
ball_speed_x = 4 * random.choice([-1, 1])  # Randomize the ball's horizontal speed (positive or negative)
ball_speed_y = -4  # Set the initial vertical speed of the ball

# Brick settings
brick_rows = 5  # Number of brick rows
brick_cols = 8  # Number of brick columns
brick_width = WIDTH // brick_cols - 5  # Set the width of each brick
brick_height = 30  # Set the height of each brick
bricks = []  # Create an empty list to store all bricks
for row in range(brick_rows):
    for col in range(brick_cols):
        # Create a rectangle for each brick and add it to the list
        bricks.append(pygame.Rect(col * (brick_width + 5), row * (brick_height + 5), brick_width, brick_height))

# Game settings
clock = pygame.time.Clock()  # Create a clock object to manage frame rate
running = True  # A flag to keep the game running
score = 0  # Initialize the score

while running:
    screen.fill(BLACK)  # Fill the screen with the black color to clear it every frame
    
    # Handle user input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user closes the window
            running = False  # Set running to False to exit the game loop
    
    # Paddle controls (move left or right)
    keys = pygame.key.get_pressed()  # Get the currently pressed keys
    if keys[pygame.K_LEFT] and paddle_x > 0:  # If the left arrow key is pressed and the paddle is not at the left edge
        paddle_x -= paddle_speed  # Move the paddle left
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:  # If the right arrow key is pressed and the paddle is not at the right edge
        paddle_x += paddle_speed  # Move the paddle right
    
    # Move the ball
    ball_x += ball_speed_x  # Update the ball's horizontal position
    ball_y += ball_speed_y  # Update the ball's vertical position
    
    # Check for ball-wall collisions
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius * 2:  # If the ball hits the left or right wall
        ball_speed_x *= -1  # Reverse the horizontal speed
    if ball_y <= 0:  # If the ball hits the top wall
        ball_speed_y *= -1  # Reverse the vertical speed
    
    # Check for ball-paddle collision
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)  # Define the paddle rectangle
    ball_rect = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)  # Define the ball rectangle
    if ball_rect.colliderect(paddle_rect):  # If the ball collides with the paddle
        ball_speed_y *= -1  # Reverse the vertical speed
    
    # Check for ball-brick collision
    for brick in bricks[:]:  # Iterate over a copy of the bricks list to avoid modifying it while iterating
        if ball_rect.colliderect(brick):  # If the ball collides with a brick
            bricks.remove(brick)  # Remove the brick from the list
            ball_speed_y *= -1  # Reverse the vertical speed of the ball
            score += 10  # Increase the score by 10
            break  # Stop checking for further collisions with bricks
    
    # Check for losing condition (ball falls below the screen)
    if ball_y >= HEIGHT:  # If the ball goes past the bottom of the screen
        print("Game Over! Score:", score)  # Print the score when the game ends
        running = False  # Stop the game loop
    
    # Draw game elements
    pygame.draw.rect(screen, WHITE, paddle_rect)  # Draw the paddle
    pygame.draw.ellipse(screen, WHITE, ball_rect)  # Draw the ball
    for brick in bricks:  # Draw each brick with a random color
        pygame.draw.rect(screen, random.choice(COLORS), brick)
    
    # Update the display to show the latest frame
    pygame.display.update()
    clock.tick(60)  # Set the frame rate to 60 FPS

# Quit pygame when the game ends
pygame.quit()
