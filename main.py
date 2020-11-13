# PyGame template.

# Import standard modules.
import math
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *

import grid
import tower
from grid import Grid
from tower import Tower

FPS = 144.0

# Define a sprite list
tower_list = pygame.sprite.Group()

# Initialize the grid
grid = Grid((0, 0), 15, 15, 40)

# Initialize a tower
tower = Tower()

# Set it's location
tower.rect.x = 50
tower.rect.y = 50

# Add the tower to a sprite list
tower_list.add(tower)


def update(dt):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        elif event.type == MOUSEBUTTONDOWN:
            print("CLICK!")

            # Get position of the mouse cursor
            pos = pygame.mouse.get_pos()
            # Get position of the mouse in the grid coordinates
            grid_pos = grid.get_grid_pos(pos)
            print(grid_pos)

            # On left mouse click print the value of the cell.
            if event.button == 1:
                print(grid.get_value(pygame.math.Vector2(grid_pos)))

            # On right mouse click set the cells value to 64.
            elif event.button == 3:
                grid.set_value(grid_pos, 1)

    # Handle other events as you wish.

    grid.update(dt)


def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.

    # Redraw screen here.

    # Draw the grid
    grid.draw(screen)

    tower_list.draw(screen)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = FPS
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 480, 480
    screen = pygame.display.set_mode((width, height))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1/fps  # dt is the time since last frame.
    while True:  # Loop forever!
        # You can update/draw here, I've just moved the code for neatness.
        update(dt)
        draw(screen)

        dt = fpsClock.tick(fps)


runPyGame()