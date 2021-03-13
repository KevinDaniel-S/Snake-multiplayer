import pygame, sys
from pygame.locals import *
from Fruit import Fruit
from Snake import Snake

def draw_fruit(fruit):
    pygame.draw.ellipse(screen, RED, fruit.draw_fruit())

def draw_snake(snake):
    pos = snake.getSnake()
    for block in pos:
        pygame.draw.rect(screen, snake.color, block)

GRAY = (98, 155, 98)
GREEN = (175, 215, 70)
BLUE = (70, 70, 190)
RED = (255, 30, 15)

cell_size = 30
cell_number = 20
screen_size = cell_number*cell_size

fruit = Fruit(cell_size, cell_number)
snakes = []
for i in range(4):
    snake = Snake(cell_size, i)
    snakes.append(snake)

pygame.init()
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    screen.fill(GRAY)
    draw_fruit(fruit)
    for snake in snakes:
        draw_snake(snake)
    clock.tick(60)
