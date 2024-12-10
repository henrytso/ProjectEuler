import os
import os.path
import sys
import re
from termcolor import colored

files = os.listdir()
py_files = [f for f in files if re.match(r"[0-9]+.py", f)]
solved_ids = set([int(re.search(r"[0-9]+", f).group()) for f in py_files])

if __name__ == "__main__":
    MAX_ID = 50 if len(sys.argv) == 1 else int(sys.argv[1])
    COLUMNS = 4
    ELEMENTS_PER_COLUMN = MAX_ID // COLUMNS + (1 if MAX_ID % COLUMNS > 0 else 0)

    columns = [[""] * ELEMENTS_PER_COLUMN for _ in range(COLUMNS)]

    i, j = 0, 0
    
    for id in range(1, MAX_ID + 1):
        color = "green" if id in solved_ids else "red"
        columns[i][j] = colored(id, color)

        i += (j + 1) // ELEMENTS_PER_COLUMN
        j = (j + 1) % ELEMENTS_PER_COLUMN

    for row_id in range(ELEMENTS_PER_COLUMN):
        row_tokens = list()
        for col_id in range(COLUMNS):
            row_tokens.append(columns[col_id][row_id])
        # joining colored(s, c) elements? Want to join with 3 tab characters
        print("\t".join(row_tokens))

all_files = os.listdir()
py_files = [f for f in all_files if re.match(r"[0-9]+.py", f)]
solved_ids = [re.search(r"[0-9]+", f) for f in py_files]
