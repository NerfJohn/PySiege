################################################################################
# DataModel.py
################################################################################

from pygame.event import Event

################################################################################
# Model of central data.
class DataModel():
    # Identity.
    m_prgmName = ""    # str: name of the program

    # State machine.
    m_doExit   = False # bool: force program to exit 

    # Defaults.
    def __init__(self):
        self.m_prgmName = "PySiege.py"
        self.m_doExit   = False
    def __str__(self):
        return f"(prgmName = {self.m_prgmName}, " + \
                f"doExit = {self.m_doExit})"
