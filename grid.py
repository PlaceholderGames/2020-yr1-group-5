import math as m

import pygame
from pygame import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Grid:
    # Position of the upper left corner
    initPos = math.Vector2
    # Number of columns
    width = None
    # Number of rows
    height = None
    # Size of each cell
    cellSize = None

    cells = list()

    cellColor = WHITE

    def __init__(self, initPos=math.Vector2(0, 0), width: int = 10, height: int = 10, cellSize: int = 25, debug=True):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.initPos = initPos
        self.cells = [[0 for j in range(height)] for i in range(width)]
        self.debug = debug

    def getWorldPos(self, pos):
        return (math.vector2(pos) * self.cellSize) + self.initPos

    def getGridPos(self, pos):
        x = m.floor((pos[0] - self.initPos[0]) / self.cellSize)
        y = m.floor((pos[1] - self.initPos[1]) / self.cellSize)
        return math.Vector2(x, y)

    def setValue(self, grid_pos, value):
        self.cells[int(grid_pos[0])][int(grid_pos[1])] = value

    def getValue(self, grid_pos):
        return self.cells[int(grid_pos[0])][int(grid_pos[1])]

    # This function needs to be called from the draw function in main.
    def draw(self, screen):
        # These for loops draw the grid using rectangles
        for x in range(self.width):
            for y in range(self.height):
                if self.debug:
                    if self.cells[x][y] == 0:
                        self.cellColor = WHITE
                    else:
                        self.cellColor = RED
                else:
                    self.cellColor = WHITE

                rect = pygame.Rect((x * self.cellSize) + self.initPos[0],
                                   (y * self.cellSize) + self.initPos[1],
                                   self.cellSize, self.cellSize)
                pygame.draw.rect(screen, self.cellColor, rect, 1)

    def update(self, dt):
        pass
