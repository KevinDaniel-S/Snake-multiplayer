from pygame import Rect
from pygame.math import Vector2

class Snake: 
    def __init__(self, cell_size):
        self.body = [Vector2(5, 10), Vector2(5, 11), Vector2(5, 12)]
        self.cell_size = cell_size
    
    def getSnake(self):
        fruit_rects = []
        for block in self.body:
            fruit_rect = Rect(int(block.x * self.cell_size), 
                int(block.y * self.cell_size),
                self.cell_size, self.cell_size)
            fruit_rects.append(fruit_rect)
        return fruit_rects
