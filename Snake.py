from pygame import Rect
from pygame.math import Vector2

RED = (183, 70, 70)
GREEN = (126, 183, 69)
CYAN = (69, 183, 183)
VIOLET = (126, 69, 183)

players_body = [[Vector2(5,   3), Vector2(4 ,  3), Vector2(3 , 3)],
                [Vector2(17,  5), Vector2(17,  4), Vector2(17, 3)],
                [Vector2(15, 17), Vector2(16, 17), Vector2(17, 17)],
                [Vector2(3,  15), Vector2(3 , 16), Vector2(3 , 17)]]

players_color = [RED, GREEN, CYAN, VIOLET] 

class Snake: 
    def __init__(self, cell_size, player):
        self.body = players_body[player]
        self.color = players_color[player]
        self.cell_size = cell_size
        self.is_alive = True
        self.direction = Vector2(0, 1)
    
    def get_snake(self):
        fruit_rects = []
        for block in self.body:
            x = int(block.x * self.cell_size)
            y = int(block.y * self.cell_size)
            fruit_rect = Rect(x, y, self.cell_size, self.cell_size)
            fruit_rects.append(fruit_rect)
        return fruit_rects

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
