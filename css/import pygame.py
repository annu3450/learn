import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Load images
car_image = pygame.image.load("car.png")
car_width = 80
car_height = 160

# Set up car initial position
car_x = (screen_width - car_width) // 2
car_y = screen_height - car_height - 20
car_speed = 5

# Set up enemy car
enemy_image = pygame.image.load("enemy_car.png")
enemy_width = 80
enemy_height = 160

enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
        car_x += car_speed

    # Update enemy car position
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height

    # Collision detection
    if car_y < enemy_y + enemy_height and car_y + car_height > enemy_y:
        if car_x < enemy_x + enemy_width and car_x + car_width > enemy_x:
            running = False

    # Refresh the screen
    window.fill((255, 255, 255))
    window.blit(car_image, (car_x, car_y))
    window.blit(enemy_image, (enemy_x, enemy_y))
    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
