################################################################################
# GuiFuncs.py
################################################################################

import pygame

from DataModel import DataModel

################################################################################

# Screen sizing.
X_SIZE = 600
Y_SIZE = 400

# Text box sizing.
TEXT_OFFSET = 30


################################################################################

# Screen/GUI.
g_screen = None

# Log/Command Font.
g_textFont = None

################################################################################
# Init GUI for use (AFTER pygame.init()).
def init_gui():
    # Ref globals for init.
    global g_screen
    global g_textFont

    # Init globals.
    g_screen   = pygame.display.set_mode((X_SIZE, Y_SIZE))
    g_textFont = pygame.font.SysFont("Courier New", 18)

################################################################################
# Process model w.r.t. GUI.
def process_gui(model: DataModel):
    # Render background.
    g_screen.fill((0, 0, 0))

    # Draw CLI (if in mode).
    if model.m_cmdOpen:
        draw_cli(model)

    # Draw log.
    draw_log_box(model)

    # Show drawn screen.
    pygame.display.flip()

################################################################################
# Updates CLI visual (without draw/flip).
def draw_cli(model: DataModel):
    # Starting cordinates.
    cords = (0, Y_SIZE - (2*TEXT_OFFSET))
    rect  = (0, Y_SIZE - (2*TEXT_OFFSET), X_SIZE, TEXT_OFFSET)

    # Draw background.
    pygame.draw.rect(g_screen,(20, 20, 20), rect)

    # Render text.
    logBox = g_textFont.render(f"CMD: {model.m_cmdBuf}", True, (255, 255, 255))
    g_screen.blit(logBox, cords)

################################################################################
# Updates log box visual (without draw/flip).
def draw_log_box(model: DataModel):
    # Starting cordinates.
    cords = (0, Y_SIZE - TEXT_OFFSET)
    rect  = (0, Y_SIZE - TEXT_OFFSET, X_SIZE, TEXT_OFFSET)

    # Draw background.
    pygame.draw.rect(g_screen,(30, 30, 30), rect)

    # Render text.
    logBox = g_textFont.render(f"LOG: {model.m_logBuf}", True, (255, 255, 255))
    g_screen.blit(logBox, cords)
