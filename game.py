import pygame, sys
from pygame.locals import *
from pygame.math import Vector2
from Fruit import Fruit
from Snake import Snake

def draw_fruit(fruit):
    pygame.draw.ellipse(screen, RED, fruit.draw_fruit())

def draw_snake(snake):
    pos = snake.get_snake()
    for block in pos:
        pygame.draw.rect(screen, snake.color, block)

class Main:
    def __init__(self, players:"int 1:4"):
        self.snakes = []
        self.fruit = Fruit(cell_size, cell_number)
        for i in range(players):
            snake = Snake(cell_size, i)
            self.snakes.append(snake)

    def update(self):
        for snake in self.snakes:
            snake.move_snake()

    def draw_elements(self):
        draw_fruit(self.fruit)
        for snake in self.snakes:
            draw_snake(snake)


GRAY = (98, 155, 98)
GREEN = (175, 215, 70)
BLUE = (70, 70, 190)
RED = (255, 30, 15)

cell_size = 30
cell_number = 20
screen_size = cell_number*cell_size

pygame.init()
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main(4)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                for snake in main_game.snakes:
                    snake.direction = Vector2(0, -1)
            if event.key == K_DOWN:
                for snake in main_game.snakes:
                    snake.direction = Vector2(0, 1)
            if event.key == K_LEFT:
                for snake in main_game.snakes:
                    snake.direction = Vector2(-1, 0)
            if event.key == K_RIGHT:
                for snake in main_game.snakes:
                    snake.direction = Vector2(1, 0)
       
    
    screen.fill(GRAY)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
