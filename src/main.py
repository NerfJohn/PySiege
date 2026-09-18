################################################################################
# main.py
################################################################################

import pygame
from pygame.locals import *

from DataModel import DataModel
from StateFuncs import process_StateMachine

################################################################################

# FPS of program.
MAIN_FPS = 60

################################################################################
# Gather/sync inputs.
def collect_inputs(model: DataModel):
    # Reset keyboard presses.
    model.m_keyEvt  = None
    model.m_keyQuit = False

    # Check pygame events.
    for event in pygame.event.get():
        # Collect keyboard presses.
        if event.type == QUIT:
            model.m_keyQuit = True
        elif event.type == KEYDOWN:
            model.m_keyEvt = event

################################################################################
# Process current states + inputs together.
def process_data(model: DataModel):
    # Run state evaluation.
    process_StateMachine(model)

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
        # INPUT-PROCESS-OUTPUT loop.
        collect_inputs(model)
        process_data(model)

        # Maintain framerate.
        clock.tick(MAIN_FPS)

    # Shutdown program.
    pygame.quit()
