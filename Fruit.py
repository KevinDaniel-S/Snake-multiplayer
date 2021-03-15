import random
from pygame import Rect
from pygame.math import Vector2

class Fruit:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)        
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = Rect(int(self.pos.x * self.cell_size), 
                int(self.pos.y * self.cell_size),
                self.cell_size, self.cell_size)
        return fruit_rect

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)        
        self.pos = Vector2(self.x, self.y)

