################################################################################
# DataModel.py: central/shared of the entire program.
################################################################################

from pygame.event import Event

################################################################################
# Model of central data.
class DataModel():
    # Identity.
    m_prgmName   = ""    # str: name of the program

    # State Machine.
    m_gettingCmd = False # bool: direct keyboard input to command vs controls.

    # Keyboard input.
    m_keyEvt     = None  # Event: latest key-press event

    # Command input.
    m_cmdBuffer  = ""    # str: command being created/executed
    m_cmdRdy     = False # bool: command creation vs ready to execute

    # Defaults.
    def __init__(self):
        self.m_prgmName   = "PySiege.py"
        self.m_gettingCmd = False
        self.m_keyEvt     = None
        self.m_cmdBuffer  = ""
        self.m_cmdRdy     = False
    def __str__(self):
        return f"(prgmName = {self.m_prgmName}, "     \
                f"gettingCmd = {self.m_gettingCmd}, " \
                f"keyEvt = {self.m_keyEvt}, "         \
                f"cmdBuffer = {self.m_cmdBuffer}, "   \
                f"cmdRdy = {self.m_cmdRdy})"

    # Converts.
    def keyEvt(self) -> Event:
        return self.m_keyEvt
