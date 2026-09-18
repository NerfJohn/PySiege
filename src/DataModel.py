################################################################################
# DataModel.py
################################################################################

from pygame.event import Event

from AppState_e import AppState_e as state

################################################################################
# Model of central data.
class DataModel():
    # Identity.
    m_prgmName = ""            # str: name of the program

    # State machine.
    m_curState = state.INPUT   # enum: current state of the program
    m_prvState = state.INVALID # enum: previous state (ie last iteration)
    m_doExit   = False         # bool: force program to exit

    # Inputs.
    m_keyEvt   = None          # Event: last key pressed (Falling edge- None if cleared)
    m_keyQuit  = False         # bool: quit key pressed (Falling edge)

    # Defaults.
    def __init__(self):
        self.m_prgmName = "PySiege.py"
        self.m_curState = state.INPUT
        self.m_prvState = state.INVALID
        self.m_doExit   = False
        self.m_keyEvt   = None
        self.m_keyQuit  = False
    def __str__(self):
        return f"(prgmName = {self.m_prgmName}, " + \
                f"curState = {self.m_curState}, " + \
                f"prvState = {self.m_prvState}, " + \
                f"doExit = {self.m_doExit}, "     + \
                f"keyEvt = {self.m_keyEvt}, "     + \
                f"keyQuit = {self.m_doQuit})"
