import os
import pygame


class Enemy(pygame.sprite.Sprite):

    health = 3
    enemyKilledEvent = pygame.event.Event(pygame.USEREVENT + 2)

    # Placeholder is towerDefense_tile271.png
    def __init__(self, image=os.path.join('Assets', 'enemy_1_64.png'), size=64):
        super().__init__()

        self.size = size

        # Load an image to display
        self.image = pygame.image.load(image)

        # Change the scale of the sprite
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        #self.image = pygame.transform.rotate(self.image, -180)

    def update(self, dt, projectiles) -> None:
        self.rect.x -= 0.2 * dt

        # get all collisions with projectiles and kill the projectile
        collisions = pygame.sprite.spritecollide(self, projectiles, True)

        # if there is any collision decrease the health of the enemy
        if len(collisions) > 0:
            self.health -= 1

        # if the health is 0 or lower kill the enemy and send an event
        # so we can react to the death
        if self.health <= 0:
            self.kill()
            pygame.event.post(self.enemyKilledEvent)
