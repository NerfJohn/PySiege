################################################################################
# MapTile.py
################################################################################

import pygame

import random

from Domain.TileType_e import TileType_e as tile

################################################################################
# Single tile within larger map (i.e. "chunk")
class MapTile():
    # Consts.
    SQUARE_MAX_LEN = 32

    # Variables.
    m_tileType = tile.PLAINS

    # Defaults.
    def __init__(self):
        self.m_tileType = tile.PLAINS
    def __str__(self):
        return f"(tileType = {self.m_tileType})"

    # Custom.
    def draw(self, screen, x_cord, y_cord):
        # Get color.
        color = (226, 28, 226) # Default "fuchisa stands out"
        if   self.m_tileType == tile.PLAINS: color = (28, 226, 102)
        elif self.m_tileType == tile.SEA:    color = (9, 105, 178)
        elif self.m_tileType == tile.MTN:    color = (49, 50, 53)

        # Draw.
        rect = (x_cord, y_cord, self.SQUARE_MAX_LEN, self.SQUARE_MAX_LEN)
        pygame.draw.rect(screen, color, rect)
