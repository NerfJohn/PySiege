################################################################################
# DataModel.py: central/shared of the entire program.
################################################################################

################################################################################
# Model of central data.
class DataModel():
    # Identity.
    m_prgmName = "" # str: name of the program

    # Funcs.
    def __init__(self):
        self.m_prgmName = "PySiege.py"
    def __str__(self):
        return f"(prgmName = {self.m_prgmName})"
