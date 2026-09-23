################################################################################
# StateFuncs.py
################################################################################

from pygame.locals import *
from typing import List

from Domain.DataModel import DataModel

################################################################################
# Process model w.r.t. CLI.
def process_cli(model: DataModel):
    # Process keys as allowed.
    if model.m_cmdOpen and (None != model.m_keyEvt):
        # Process key.
        if K_RETURN == model.m_keyEvt.key:
            model.m_cmdRdy = True
        elif K_BACKSPACE == model.m_keyEvt.key:
            model.m_cmdBuf[:-1]
        elif model.m_keyEvt.unicode and model.m_keyEvt.unicode.isprintable():
            model.m_cmdBuf += str.lower(model.m_keyEvt.unicode)

    # Run command as allowed.
    if model.m_cmdRun:
        execute_command(model)
        model.m_cmdRst = True

    # Reset command as allowed.
    if model.m_cmdRst:
        reset_cli(model)
    

################################################################################
# Reset CLI portion of model.
def reset_cli(model: DataModel):
    model.m_cmdRun = False
    model.m_cmdRst = False
    model.m_cmdBuf = ""
    model.m_cmdRdy = False

################################################################################
# Execute commnand (from data model).
def execute_command(model: DataModel):
    # Convert command to string list.
    argv = [w for w in model.m_cmdBuf.split(" ") if w.strip()]

    # Run handler.
    if len(argv):
        cmd = argv[0]
        if "mdl" == cmd: cli_mdl(argv[1:], model)
        if "cls" == cmd: cli_cls(argv[1:], model)
        else:
            print(f"Unknown Command: {cmd}")

    # Reset CLI.
    reset_cli(model)

################################################################################
# CLI command to print data model.
def cli_mdl(args: List[str], model: DataModel):
    model.m_logBuf = model.__str__()
    print(model)

################################################################################
# CLI command to print data model.
def cli_cls(args: List[str], model: DataModel):
    model.m_logBuf = ""
    print("cleared log")
