#TODO: implement snake movement using direction variable and probably dictionary functions

import pygame
pygame.init()
width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True

x1 = width / 2
y1 = height / 2
x2 = x1 + 20
y2 = y1
x3 = x2 + 20
y3 = y2

global snake_body
snake_body = [(x1, y1), (x2, y2), (x3, y3)]
direction = "LEFT"

def move_left():
    snake_body.insert(0, (snake_body[0][0] - 20, snake_body[0][1]))
    snake_body.pop()

def move_right():
    snake_body.insert(0, (snake_body[0][0] + 20, snake_body[0][1]))
    snake_body.pop()

def move_up():
    snake_body.insert(0, (snake_body[0][0], snake_body[0][1] - 20))
    snake_body.pop()

def move_down():
    snake_body.insert(0, (snake_body[0][0], snake_body[0][1] + 20))
    snake_body.pop()

while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for x, y in snake_body:
        pygame.draw.rect(screen, "white", pygame.Rect(x, y, 15, 15))
    
    move_right()

    pygame.display.update()

    clock.tick(4)

pygame.quit()

