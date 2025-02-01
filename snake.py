#TODO: Improve movement and code food, implement score and game over conditions.
#BUG: Fast keypresses allows a 180, limit input to one per frame.
#BUG: Update food and snake immediately after eating. Currently, snake head moves onto food, takes a frame to process. Delayed.

import pygame
import random
pygame.init()
width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
running = True

# Starting position of snake
x1 = 640
y1 = 360
x2 = x1 + 20
y2 = y1
x3 = x2 + 20
y3 = y2

# Snake position and direction tracking
global snake_body
snake_body = [(x1, y1), (x2, y2), (x3, y3)]
direction = "LEFT"

# Apple tracking
apple_pos_x = random.randint(0, width - 20) // 20 * 20
apple_pos_y = random.randint(0, height - 20) // 20 * 20
appleEaten = False


# Functions for moving the snake
def move_left():
    snake_body.insert(0, (snake_body[0][0] - 20, snake_body[0][1]))
    if appleEaten == False:
        snake_body.pop()

def move_right():
    snake_body.insert(0, (snake_body[0][0] + 20, snake_body[0][1]))
    if appleEaten == False:
        snake_body.pop()

def move_up():
    snake_body.insert(0, (snake_body[0][0], snake_body[0][1] - 20))
    if appleEaten == False:
        snake_body.pop()

def move_down():
    snake_body.insert(0, (snake_body[0][0], snake_body[0][1] + 20))
    if appleEaten == False:
        snake_body.pop()

# Direction dictionary
direction_actions = {
    "LEFT": move_left,
    "RIGHT": move_right,
    "UP": move_up,
    "DOWN": move_down
}


while running: 
    
    for event in pygame.event.get():
        # If user quits, running = False, stopping the loop
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if direction != "DOWN":
                    direction = "UP"
            if event.key == pygame.K_s:
                if direction != "UP":
                    direction = "DOWN"
            if event.key == pygame.K_a:
                if direction != "RIGHT":
                    direction = "LEFT"
            if event.key == pygame.K_d:
                if direction != "LEFT":
                    direction = "RIGHT"
    screen.fill("black")

    # Movement logic
    direction_actions[direction]()
    appleEaten = False
    
    # Generating the snake body
    for x, y in snake_body:
        pygame.draw.rect(screen, "white", pygame.Rect(x, y, 15, 15))
    
    # Generating food
    pygame.draw.rect(screen, "red", pygame.Rect(apple_pos_x, apple_pos_y, 15, 15))

    # Checking if snake head touches food
    if snake_body[0] == (apple_pos_x, apple_pos_y):
        print("statement true")
        appleEaten = True
        apple_pos_x = random.randint(0, width - 20) // 20 * 20
        apple_pos_y = random.randint(0, height - 20) // 20 * 20

    # Checking if snake hits wall
    if snake_body[0][0] > width or snake_body[0][1] > height or snake_body[0][0] < 0 or snake_body[0][1] < 0:
        running = False
    
    # Checking if snake hits snake
    for x in snake_body[1:]:
        if x == snake_body[0]:
            running = False


    pygame.display.update()

    clock.tick(6)

pygame.quit()

