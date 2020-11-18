# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite

import os
import pygame
import grid
from grid import Grid


class Tower(pygame.sprite.Sprite):

    def __init__(self, image=os.path.join('Assets', 'towerDefense_tile206.png'), size=64):
        super().__init__()

        self.size = size

        # Load an image to display
        self.image = pygame.image.load(image)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Change the scale of the sprite
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
