#!/usr/bin/env python

#
# -----------------------------------------------------------
#  Search for files from the command line using Pathlib
#  chibiace 08/04/2023
# -----------------------------------------------------------
#
import os
from pathlib import Path
import sys


# Prerecorded error message with red coloured warning.
def warning(text):
    RED = '\033[31m'
    END = '\033[0m'
    return RED+text+END


warningMessage = f'Please use a {warning("single word")} without wildcards to search for a file in the CWD!'


# Assign the search term to a variable
try:
    script, arg1 = sys.argv
except ValueError:
    # Throws a warning if too many command line arguments and exits
    print(warningMessage)
    sys.exit()


# Search function
def pathsearch(filename, path=os.getcwd()):
    result = []
    for file in Path(path).rglob(filename):
        result.append(os.fspath(file))
        print(os.fspath(file))
    return result


# Call function with argument
results = []
try:
    results = pathsearch(f'*{arg1}*')
except ValueError:
    # Throws a warning if something is wrong like special characters in argument, exits.
    print(warningMessage)
    sys.exit()

