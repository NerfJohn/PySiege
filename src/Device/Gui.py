################################################################################
# Gui.py: UI screen displayed to the user.
################################################################################

import pygame

from Domain.DataModel import DataModel

################################################################################
# GUI for the program.
class Gui():
    # Consts.
    GUI_X_SIZE = 300
    GUI_Y_SIZE = 100

    # Vars.
    m_model  = None # DataModel: reference to draw/display items
    m_screen = None # Surface: pygame object representing GUI
    m_font   = None # Font: pygame font used for text display

    # Defaults.
    def __init__(self, model: DataModel):
        # Save.
        self.m_model = model

        # Setup.
        self.m_screen = pygame.display.set_mode((self.GUI_X_SIZE, self.GUI_Y_SIZE))
        pygame.display.set_caption(model.m_prgmName)
        self.m_font = pygame.font.SysFont("Courier New", 18)

    # Actions.
    def draw(self):
        # Blank canvas.
        self.m_screen.fill((30, 30, 30))
        y_offset = 20

        # Draw UI text for Command Mode
        mode_text = self.m_font.render(f"Command Mode? {str(self.m_model.m_gettingCmd)}", True, (255, 165, 0))
        self.m_screen.blit(mode_text, (20, y_offset))
        y_offset += 40
        
        # Render the current typing buffer as a command prompt
        prompt_text = self.m_font.render(f"> {self.m_model.m_cmdBuffer}_", True, (255, 255, 255))
        self.m_screen.blit(prompt_text, (20, y_offset))
        y_offset += 40

        # Show.
        pygame.display.flip()
