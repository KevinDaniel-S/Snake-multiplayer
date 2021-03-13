import pygame, sys
from pygame.locals import *
from Fruit import Fruit
from Snake import Snake

GREEN = (175, 215, 70)
BLUE = (70, 70, 190)
RED = (183, 70, 70)

cell_size = 30
cell_number = 20
screen_size = cell_number*cell_size

fruit = Fruit(cell_size, cell_number)
snake = Snake(cell_size)

pygame.init()
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()

screen.fill(GREEN)
pygame.draw.rect(screen, BLUE, fruit.draw_fruit())
pos = snake.getSnake()
for block in pos:
    print(block)
    pygame.draw.rect(screen, RED, block)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)
