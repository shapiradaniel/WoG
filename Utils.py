# Utils.py

import os

# CONST definitions
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 1


# Function clear screen
def screen_cleaner(lines=100):
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print('\n' * lines)
