import os
import pygame


class Enemy(pygame.sprite.Sprite):

    health = 6

    def __init__(self, image=os.path.join('Assets', 'towerDefense_tile271.png'), size=64):
        super().__init__()

        self.size = size

        # Load an image to display
        self.image = pygame.image.load(image)

        # Change the scale of the sprite
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.image = pygame.transform.rotate(self.image, -180)

    def update(self, dt, projectiles) -> None:
        self.rect.x -= 0.2 * dt

        collisions = pygame.sprite.spritecollide(self, projectiles, True)

        if len(collisions) > 0:
            self.health -= 1

        if self.health <= 0:
            self.kill()
