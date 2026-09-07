################################################################################
# main.py: root of the program- setup and loop functions.
################################################################################

import pygame
from pygame.locals import *

from Domain.DataModel import DataModel

################################################################################

# FPS of program.
MAIN_FPS = 60

################################################################################
# Start of program.
if __name__ == "__main__":
    # Init central data.
    model = DataModel()

    # Init pygame details.
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption(model.m_prgmName)
    clock = pygame.time.Clock()

    # Main loop.
    running = True
    while running:
        # INPUT: Get keyboard input.
        for event in pygame.event.get():
            # Exit scenarios.
            if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
                running = False

            # Key presses (grab first for processing).
            if (event.type == KEYDOWN) and (model.keyEvt() == None):
                model.m_keyEvt = event

        # PROCESS: keyboard inputs.
        keyEvt = model.keyEvt()
        if keyEvt != None:
            # Keyboard vs command.
            if model.m_gettingCmd:
                if keyEvt.key == K_RETURN:
                    model.m_cmdRdy = True
                elif keyEvt.key == K_BACKSPACE:
                    model.m_cmdBuffer = model.m_cmdBuffer[:-1]
                elif keyEvt.unicode and keyEvt.unicode.isprintable():
                    model.m_cmdBuffer += keyEvt.unicode
            else:
                if keyEvt.key == K_SLASH:
                    print("Intake command...")
                    model.m_gettingCmd = True
                else:
                    print(f"Key pressed: {pygame.key.name(keyEvt.key)}")  # Prints the key name
            model.m_keyEvt = None

        # OUTPUT: run command.
        if model.m_cmdRdy:
            print(f"Run Command: {model.m_cmdBuffer}")
            model.m_cmdBuffer  = ""
            model.m_cmdRdy     = False
            model.m_gettingCmd = False

        # MAINTENANCE: Maintain framerate.
        clock.tick(MAIN_FPS)

    # Shutdown program.
    pygame.quit()
