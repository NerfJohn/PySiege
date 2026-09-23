################################################################################
# DataModel.py
################################################################################

from pygame.event import Event

from Domain.AppState_e import AppState_e as state

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
    m_keyQuit  = False         # bool:  quit key pressed (Falling edge)

    # CLI Implement.
    m_cmdOpen  = False         # bool: control to allow CLI to append key events
    m_cmdRun   = False         # bool: control to allow CLI to run command
    m_cmdRst   = False         # bool: control to allow CLI to be reset
    m_cmdBuf   = ""            # str:  command to receive/execute
    m_cmdRdy   = False         # bool: indicator of command buffer being ready to execute

    # GUI Implements.
    m_logBuf   = ""            # str: text to show in the GUI's log box

    # Defaults.
    def __init__(self):
        self.m_prgmName = "PySiege.py"
        self.m_curState = state.INPUT
        self.m_prvState = state.INVALID
        self.m_doExit   = False
        self.m_keyEvt   = None
        self.m_keyQuit  = False
        self.m_cmdOpen  = False
        self.m_cmdRun   = False
        self.m_cmdRst   = False
        self.m_cmdBuf   = ""
        self.m_cmdRdy   = False
        self.m_logBuf   = ""
    def __str__(self):
        return f"(prgmName = {self.m_prgmName}, " + \
                f"curState = {self.m_curState}, " + \
                f"prvState = {self.m_prvState}, " + \
                f"doExit = {self.m_doExit}, "     + \
                f"keyEvt = {self.m_keyEvt}, "     + \
                f"keyQuit = {self.m_keyQuit}, "   + \
                f"cmdOpen = {self.m_cmdOpen}, "   + \
                f"cmdRun = {self.m_cmdRun}, "     + \
                f"cmdRst = {self.m_cmdRst}, "     + \
                f"cmdBuf = {self.m_cmdBuf}, "     + \
                f"cmdRdy = {self.m_cmdRdy}, "     + \
                f"logBuf = {self.m_logBuf})"
