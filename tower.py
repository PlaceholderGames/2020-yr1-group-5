# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite

import os, pygame
import grid
from grid import Grid

class Tower(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        # Load an image to display
        self.image = pygame.image.load(os.path.join('Assets', 'towerDefense_tile206.png'))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self, dt):
        pass

    def place_on_grid(self, grid: Grid):
        # I want to draw the tower on the grid outside the Grid class. The Grid class should only take care of the basic grid functionality.
        for x in range(grid.width):
            for y in range(grid.height):
                pass