import pygame, sys, os
from pygame.locals import *
from pygame.math import Vector2
from Fruit import Fruit
from Snake import Snake

x, y = 50, 50

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def make_move(key):
    directions = {K_UP:Vector2(0, -1), K_DOWN:Vector2(0, 1),
             K_LEFT:Vector2(-1, 0), K_RIGHT:Vector2(1, 0)}
    if key in directions:
        for snake in main_game.snakes:
            direction = directions[key]
            if snake.direction + direction != Vector2(0, 0):
                snake.direction = directions[key]

def draw_fruit(fruit):
    pygame.draw.ellipse(screen, RED, fruit.draw_fruit())

def draw_snake(snake):
    pos = snake.get_snake()
    for block in pos:
        pygame.draw.rect(screen, snake.color, block)

class Main:
    def __init__(self, players:"int 1:4"):
        if players not in range(1, 5):
            raise("Número de jugadores no valido")
        self.players = players
        self.snakes = []
        self.fruits = []
        self.textsurface = myfont.render('', False, (0, 0, 0))
        for i in range(players):
            snake = Snake(cell_size, i)
            fruit = Fruit(cell_size, cell_number)
            self.fruits.append(fruit)
            self.snakes.append(snake)

    def update(self):
        for snake in self.snakes:
            snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        for fruit in self.fruits:
            draw_fruit(fruit)
        for snake in self.snakes:
            draw_snake(snake)
        self.draw_score()

    def check_collision(self):
        for snake in self.snakes:
            for fruit in self.fruits:
                if fruit.pos in snake.body[1:]:
                    fruit.randomize()
                if snake.body[0] == fruit.pos:
                    fruit.randomize()
                    snake.add_block()

    def check_fail(self):
        bodies = [snake.body[1:] for snake in self.snakes] 
        pos = [item for sublist in bodies for item in sublist]
        for snake in self.snakes:
            if (not 0 <= snake.body[0].x < cell_number or 
                    not 0 <= snake.body[0].y < cell_number):
                if snake.is_alive:
                    snake.die()
                    self.players -= 1
            if snake.body[0] in pos:
                if snake.is_alive:
                    snake.die()
                    self.players -= 1
        if self.players == 0:
            winner = 0
            best = 0
            for snake in self.snakes:
                len_snake = len(snake.body)
                if len_snake > best:
                    best = len_snake
                    winner = snake.player
            self.textsurface = myfont.render(f'Game over  Winner is player: {winner+1}', True, (0, 0, 0))

    def draw_score(self):
        score_x = int(cell_size * cell_number - 200)
        score_y = int(cell_size * cell_number - 40)
        for snake in self.snakes:
            score = len(snake.body)-3
            score_surface = myfont.render(str(score), True, (56, 74, 12))
            score_rect = score_surface.get_rect(center = (score_x, score_y))
            color_rect = score_surface.get_rect(center = (score_x, score_y+20))
            screen.blit(score_surface, score_rect)
            pygame.draw.rect(screen, snake.original, color_rect)
            score_x += 40


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
            make_move(event.key)       
    
    screen.fill(GRAY)
    main_game.draw_elements()
    screen.blit(main_game.textsurface,(150, 150))
    pygame.display.update()
    clock.tick(60)
