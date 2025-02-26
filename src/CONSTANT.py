import os
from UTILITY import logln_info

# ---
# Workspace paths
# ---
__SOURCE_FOLDER_PATH: str = os.path.dirname(__file__)
__DATA_FOLDER_PATH: str = os.path.join(os.path.dirname(__file__), "DATA")
__WORK_FOLDER_PATH: str = os.path.join(os.path.dirname(__file__), "WORK")
__FLASK_FOLDER_PATH: str = os.path.join(os.path.dirname(__file__), "WORK")


# ---
# String constants
# ---
__SEPARATOR: str =  50 * "-" 


if __name__ == "__main__":
    logln_info(__SEPARATOR)
    logln_info("Übersicht über alle definierten Konstanten:")
    logln_info(__SEPARATOR)
    constants = {
        name: value for name, value in globals().items() if name.lstrip("_").isupper()
    }
    for name, value in constants.items():
        logln_info(f"{name} = {value}")
    logln_info(__SEPARATOR)
    
