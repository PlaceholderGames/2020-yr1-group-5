import os
import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, image=os.path.join('Assets', 'towerDefense_tile295.png'), size=64):
        super().__init__()

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
        self.rect.x += 0.5 * dt
        if self.rect.x > grid.width * grid.cellSize:
            self.kill()
