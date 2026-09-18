################################################################################
# main.py
################################################################################

import pygame
from pygame.locals import *

from DataModel import DataModel

################################################################################

# FPS of program.
MAIN_FPS = 60

################################################################################
# Start of program.
if __name__ == "__main__":
    # Init central model.
    model = DataModel()

    # Init pygame details.
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock  = pygame.time.Clock()

    while False == model.m_doExit:
        for event in pygame.event.get():
            # Exit scenarios.
            if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
                model.m_doExit = True

        # Maintain framerate.
        clock.tick(MAIN_FPS)

    # Shutdown program.
    pygame.quit()
