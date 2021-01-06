# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite

import os
import pygame
import grid
from grid import Grid


class Tower(pygame.sprite.Sprite):

    # Placeholder is towerDefense_tile249.png
    def __init__(self, image=os.path.join('Assets', 'turret1_64.png'), size=64):
        super().__init__()

        self.size = size

        # Load an image to display
        self.image = pygame.image.load(image)

        # Change the scale of the sprite
        #self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Rotate the sprite so it is facing the right way.
        #self.image = pygame.transform.rotate(self.image, -90)

        # Preparation for use of a sprite sheet.
        # If the file is already 64x64 nothing happens.
        #self.image = pygame.Surface.subsurface(self.image, (0, 0), (64, 64))

        # Declare custom event
        self.myEvent = pygame.event.Event(pygame.USEREVENT+3, tower=self)
        # Declare the shoot interval
        self.shootInterval = 1.75
        # Set the initial value of the timer
        self.timer = self.shootInterval

    def update(self, dt) -> None:
        # Post the shoot event every given interval.
        self.timer -= dt/1000
        if self.timer < 0:
            pygame.event.post(self.myEvent)
            # set the timer back to the interval
            self.timer = self.shootInterval
