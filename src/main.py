################################################################################
# main.py
################################################################################

import pygame
from pygame.locals import *

from DataModel import DataModel
from GuiFuncs import init_gui, process_gui
from CliFuncs import process_cli
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
    # Process CLI.
    process_cli(model)

    # Run state evaluation.
    process_StateMachine(model)

################################################################################
# Drive outputs.
def drive_outputs(model: DataModel):
    # Draw screen.
    process_gui(model)

################################################################################
# Start of program.
if __name__ == "__main__":
    # Init pygame details.
    pygame.init()
    pygame.font.init()
    clock  = pygame.time.Clock()
    init_gui()

    # Init central model.
    model = DataModel()

    while False == model.m_doExit:
        # INPUT-PROCESS-OUTPUT loop.
        collect_inputs(model)
        process_data(model)
        drive_outputs(model)

        # Maintain framerate.
        clock.tick(MAIN_FPS)

    # Shutdown program.
    pygame.quit()
