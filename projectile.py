import os
import pygame


class Projectile(pygame.sprite.Sprite):

    def rotCenter(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    # Placeholder: towerDefense_tile295.png
    def __init__(self, image=os.path.join('Assets', 'controller.png'), size=64):
        super().__init__()

        self.speed = 0.2
        self.rotationSpeed = 1

        self.size = size

        # Load an image to display
        self.image = pygame.image.load(image)

        # Change the scale of the sprite
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.image = pygame.transform.rotate(self.image, 90)

    def update(self, dt, grid) -> None:

        '''rotation = 0
        rotation += self.rotationSpeed

        self.image = self.rotCenter(self.image, rotation)'''

        self.rect.x += self.speed * dt

        if self.rect.x > grid.width * grid.cellSize:
            self.kill()
