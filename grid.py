import math as m

import pygame
from pygame import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Grid():
    # Position of the upper left corner
    init_pos = math.Vector2
    # Number of columns
    width = None
    # Number of rows
    height = None
    # Size of each cell
    cell_size = None

    cells = list()

    color = WHITE

    def __init__(self, init_pos=math.Vector2(0, 0), width=None, height=None, cell_size=None):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.init_pos = init_pos
        self.cells = [[0 for j in range(width)] for i in range(height)]

    def get_world_pos(self, pos):
        return (math.vector2(pos) * self.cell_size) + self.init_pos

    def get_grid_pos(self, pos):
        x = m.floor((pos[0] - self.init_pos[0])/self.cell_size)
        y = m.floor((pos[1] - self.init_pos[1])/self.cell_size)
        return math.Vector2(x, y)

    # Not sure it's working
    def set_value(self, grid_pos, value):
        self.cells[int(grid_pos[0])][int(grid_pos[1])] = value

    def get_value(self, grid_pos):
        return self.cells[int(grid_pos[0])][int(grid_pos[1])]

    # This function needs to be called from the draw function in main.
    def draw(self, screen):
        # These for loops draw the grid using rectangles
        for x in range(self.width):
            for y in range(self.height):
                if self.cells[x][y] == 0:
                    self.color = WHITE
                else:
                    self.color = RED

                rect = pygame.Rect((x*self.cell_size) + self.init_pos[0],
                                   (y*self.cell_size) + self.init_pos[1],
                                   self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.color, rect, 3)

    def update(self, dt):
        pass
