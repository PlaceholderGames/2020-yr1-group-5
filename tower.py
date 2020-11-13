# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite

import os, pygame

class Tower(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        # Load an image to display
        self.image = pygame.image.load(os.path.join('Assets', 'towerDefense_tile206.png'))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
