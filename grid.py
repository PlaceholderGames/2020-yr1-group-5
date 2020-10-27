import pygame

WHITE = (255,255,255)

class Grid():
    # Position of the upper left corner
    init_pos = (0,0)
    # Number of columns
    width = None
    # Number of rows
    height = None
    # Size of each cell
    cell_size = None

    def __init__(self, init_pos = (), width = None, height = None, cell_size = None):
        print("INIT!")
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.init_pos = init_pos

    # This function needs to be called from the draw function in main.
    def draw(self, screen):

        # These for loops draw the grid using rectangles with white border
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect((x*self.cell_size) + self.init_pos[0], 
                                (y*self.cell_size) + self.init_pos[1],
                                self.cell_size, self.cell_size)
                pygame.draw.rect(screen, WHITE, rect, 1)