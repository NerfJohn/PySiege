################################################################################
# StateFuncs.py
################################################################################

from pygame.locals import *
import sys

from AppState_e import AppState_e as state
from DataModel import DataModel

################################################################################
# Root for running state machine evaluations.
def process_StateMachine(model: DataModel):
    # All states can be directly exited from.
    if model.m_keyQuit:
        model.m_doExit = True

    # Run specific state evaluation.
    if   state.INPUT   == model.m_curState: process_InputState(model)
    elif state.COMMAND == model.m_curState: process_CommandState(model)
    elif state.PROCESS == model.m_curState: process_ProcessState(model)
    else:
        print(f"ERROR: Unknown state '{model.m_curState}'")
        sys.exit()

################################################################################
# State evaluation for INPUT state.
def process_InputState(model: DataModel):
    # Run entry (as applicable).
    if state.INPUT != model.m_prvState:
        print("enter INPUT state")
        model.m_prvState = state.INPUT

    # Prep conditions.
    hasKey = (model.m_keyEvt != None) and (model.m_keyEvt.key != K_ESCAPE)
    doExit = (model.m_keyEvt != None) and (model.m_keyEvt.key == K_ESCAPE)
    doCmd  = (model.m_keyEvt != None) and (model.m_keyEvt.key == K_SLASH)

    # Evaluate.
    if doExit:   model.m_doExit   = True
    if doCmd:    model.m_curState = state.COMMAND # either CMD or PROC (or wait)
    elif hasKey: model.m_curState = state.PROCESS

    # Run exit (as applicable).
    if state.INPUT != model.m_curState:
        print("exit INPUT state")

################################################################################
# State evaluation for COMMAND state.
def process_CommandState(model: DataModel):
    # Run entry (as applicable).
    if state.COMMAND != model.m_prvState:
        print("enter COMMAND state")
        model.m_prvState = state.COMMAND

    # Prep conditions.
    runCmd   = (model.m_keyEvt != None) and (model.m_keyEvt.key == K_RETURN)
    doCancel = (model.m_keyEvt != None) and (model.m_keyEvt.key == K_ESCAPE)

    # Evaluate.
    if   runCmd:   model.m_curState = state.INPUT
    elif doCancel: model.m_curState = state.INPUT

    # Run exit (as applicable).
    if state.COMMAND != model.m_curState:
        print("exit COMMAND state")

################################################################################
# State evaluation for PROCESS state.
def process_ProcessState(model: DataModel):
    # Run entry (as applicable).
    if state.PROCESS != model.m_prvState:
        print("enter PROCESS state")
        model.m_prvState = state.PROCESS

    # Evaluate.
    model.m_curState = state.INPUT

    # Run exit (as applicable).
    if state.PROCESS != model.m_curState:
        print("exit PROCESS state")
