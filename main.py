# PyGame template. https://gist.github.com/MatthewJA/7544830

# Import standard modules.
import math as m
import random
import sys
import os

# Import non-standard modules.
import pygame
import pygame.freetype
from pygame.locals import *
from pygame import math

from grid import Grid
from tower import Tower
from projectile import Projectile
from enemy import Enemy

score = 100

class Game:
    FPS = 144.0

    GRID_CELL_SIZE = 64
    GRID_WIDTH = 16
    GRID_HEIGHT = 5

    # Custom events
    shootEvent = pygame.USEREVENT + 0
    spawnEnemy = pygame.USEREVENT + 1
    enemyKilled = pygame.USEREVENT + 2

    # Define lists of sprites
    towers = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()

    # Initialize the grid
    grid = Grid((0, 64), GRID_WIDTH, GRID_HEIGHT, GRID_CELL_SIZE, False)

    def update(self, dt):
        """
        Update game. Called once per frame.
        dt is the amount of time passed since last frame.
        If you want to have constant apparent movement no matter your framerate,
        what you can do is something like

        x += v * dt

        and this will scale your velocity based on time. Extend as necessary."""

        global score

        # Go through events that are passed to the script by the window.
        for event in pygame.event.get():
            # We need to handle these events. Initially the only one you'll want to care
            # about is the QUIT event, because if you don't handle it, your game will crash
            # whenever someone tries to exit.
            if event.type == QUIT:
                pygame.quit()  # Opposite of pygame.init
                sys.exit()  # Not including this line crashes the script on Windows. Possibly
                # on other operating systems too, but I don't know for sure.

            # When 'Delete' is pressed the grid is cleared
            elif event.type == KEYDOWN:
                if event.key == K_DELETE:
                    self.grid.cells = [[0 for j in range(self.grid.height)]
                                       for i in range(self.grid.width)]
                    for sprite in self.allSprites:
                        sprite.kill()

            elif event.type == MOUSEBUTTONDOWN:
                # Get position of the mouse cursor
                pos = pygame.mouse.get_pos()
                # Get position of the mouse in the grid coordinates
                grid_pos = self.grid.getGridPos(pos) if self.grid.getGridPos(
                    pos).x < self.grid.width and self.grid.getGridPos(
                    pos).y < self.grid.height else (0, 0)
                print(grid_pos)

                # On right mouse click print the value of the cell.
                if event.button == 3:
                    print(self.grid.getValue(pygame.math.Vector2(grid_pos)))

                # On left mouse click set the cells value to 64.
                elif event.button == 1:
                    if self.grid.getValue(grid_pos) != 2 and score >= 50:
                        self.grid.setValue(grid_pos, 1)
                        score -= 50

            elif event.type == self.shootEvent:
                for x in range(self.grid.width):
                    for y in range(self.grid.height):
                        if self.grid.getValue((x, y)) == 2:
                            projectile = Projectile()
                            projectile.rect.x = (x * self.grid.cellSize) + self.grid.initPos[0]
                            projectile.rect.y = (y * self.grid.cellSize) + self.grid.initPos[1]
                            self.projectiles.add(projectile)
                            self.allSprites.add(projectile)

            elif event.type == self.spawnEnemy:
                enemy = Enemy()
                enemy.rect.x = (self.grid.width * self.grid.cellSize) + 128 + self.grid.initPos[0]
                enemy.rect.y = (m.floor(random.uniform(0, self.grid.height)) * self.grid.cellSize) + self.grid.initPos[
                    1]
                self.enemies.add(enemy)
                self.allSprites.add(enemy)
                print("SPAWN")

            elif event.type == self.enemyKilled:
                score += 50

        # Handle other events as you wish.

        self.grid.update(dt)
        self.towers.update()
        self.projectiles.update(dt, self.grid)
        self.enemies.update(dt, self.projectiles)

        # Add a tower on the grid if it is supposed to be there.
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                if self.grid.getValue((x, y)) == 1:
                    tower = Tower(size=self.GRID_CELL_SIZE)
                    tower.rect.x = (x * self.grid.cellSize) + self.grid.initPos[0]
                    tower.rect.y = (y * self.grid.cellSize) + self.grid.initPos[1]
                    self.towers.add(tower)
                    self.allSprites.add(tower)
                    self.grid.setValue((x, y), 2)

    def draw(self, screen):
        """
        Draw things to the window. Called once per frame.
        """
        screen.fill((187, 128, 68))  # Fill the screen with black.

        # Redraw screen here.

        # Draw the grid
        self.grid.draw(screen)

        global score

        self.font.render_to(screen, (5, 5), "Score: ")
        self.font.render_to(screen, (182, 5), str(score))

        self.allSprites.draw(screen)

        # Flip the display so that the things we drew actually show up.
        pygame.display.flip()

    def runPyGame(self):
        # Initialise PyGame.
        pygame.init()
        pygame.freetype.init()

        self.font = pygame.freetype.SysFont("FreeSerif", 59)

        # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
        fps = self.FPS
        fpsClock = pygame.time.Clock()

        # Set up the window.
        screen = pygame.display.set_mode(((self.GRID_CELL_SIZE * self.GRID_WIDTH) + self.grid.initPos[0],
                                          (self.GRID_CELL_SIZE * self.GRID_HEIGHT) + self.grid.initPos[1]))

        # screen is the surface representing the window.
        # PyGame surfaces can be thought of as screen sections that you can draw onto.
        # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

        # Main game loop.
        dt = 1 / fps * 1000  # dt is the time since last frame.

        while True:  # Loop forever!
            # You can update/draw here, I've just moved the code for neatness.
            self.update(dt)
            self.draw(screen)

            dt = fpsClock.tick(fps)

    pygame.time.set_timer(shootEvent, 1000)
    pygame.time.set_timer(spawnEnemy, 2000)


game = Game()
game.runPyGame()
