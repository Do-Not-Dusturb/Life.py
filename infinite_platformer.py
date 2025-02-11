import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Infinite Platformer")

# Player settings
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size
player_speed = 5
player_jump = -15
gravity = 1
player_velocity_y = 0
is_jumping = False

# Platform settings
platforms = []
platform_width = 100
platform_height = 10
platform_speed = 3

# Generate initial platforms
for i in range(7):
    platform_x = random.randint(0, SCREEN_WIDTH - platform_width)
    platform_y = i * 100
    platforms.append(pygame.Rect(platform_x, platform_y, platform_width, platform_height))

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        player_velocity_y = player_jump
        is_jumping = True

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Collision with platforms
    for platform in platforms:
        if player_y + player_size > platform.y and player_y + player_size < platform.y + platform_height:
            if player_x + player_size > platform.x and player_x < platform.x + platform_width:
                player_y = platform.y - player_size
                player_velocity_y = 0
                is_jumping = False

    # Generate new platforms
    for platform in platforms:
        platform.y += platform_speed
        if platform.y > SCREEN_HEIGHT:
            platform.y = 0
            platform.x = random.randint(0, SCREEN_WIDTH - platform_width)

    # Draw player and platforms
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
