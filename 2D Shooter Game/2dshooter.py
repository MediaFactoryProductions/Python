#FIRST THING LET’S IMPORT OUR IMPORTANT LIBRARIES THAT WE’LL NEED

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
BULLET_SIZE = 5
PLAYER_SPEED = 10
ENEMY_SPEED = 3
BULLET_SPEED = 7
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Let’s also draw our player.
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_speed_x = 0

#enemies
enemies = []
ENEMY_COUNT = 5

for _ in range(ENEMY_COUNT):
    enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(-HEIGHT, 0), ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)

#bullets
bullets = []

#score & multiplier & game state
score = 0
multiplier = 1
game_over = False

# Game fonts
font = pygame.font.Font(None, 36)

#game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    #event handling for specifc events based on key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player_speed_x = PLAYER_SPEED
            elif event.key == pygame.K_SPACE:
                if game_over:
                # Reset variables for a new game
                    game_over = False
                    player.x = WIDTH // 2 - PLAYER_SIZE // 2
                    player.y = HEIGHT - 2 * PLAYER_SIZE
                    enemies = [pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(-HEIGHT, 0), ENEMY_SIZE, ENEMY_SIZE) for _ in range(ENEMY_COUNT)]
                    bullets = []
                    score = 0
                    multiplier = 1

                else:
                    bullet = pygame.Rect(player.centerx - BULLET_SIZE // 2, player.top - BULLET_SIZE, BULLET_SIZE, BULLET_SIZE)
                    bullets.append(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0

    #player position update
    if not game_over:
        player.x += player_speed_x

    # Bound the player within the window
    player.left = max(player.left, 0)
    player.right = min(player.right, WIDTH)

    # Draw the player
    pygame.draw.rect(screen, RED, player)


    for enemy in enemies:
        if not game_over:
            enemy.y += ENEMY_SPEED
            pygame.draw.rect(screen, BLUE, enemy)

        if enemy.top > HEIGHT:
            game_over = True  # Trigger game over if an enemy reaches the bottom
            break

        if enemy.colliderect(player):
            game_over = True

    # Move and draw bullets
    for bullet in bullets:
        if not game_over:
            bullet.y -= BULLET_SPEED
            pygame.draw.rect(screen, RED, bullet)

    # Check for bullet-enemy collisions
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 100 * multiplier  # Increase score for hitting an enemy
                multiplier += 1 #Our multiplier scales with the more enemies that you hit.

                new_enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(-HEIGHT, 0), ENEMY_SIZE, ENEMY_SIZE)
                enemies.append(new_enemy)

    # Display score on our canvas
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    # Display game_over text once the player loses.
    if game_over:
        game_over_text = font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))

#here we'll pass FPS to our clock.tick to achieve 60 FPS

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
