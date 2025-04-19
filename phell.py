# /usr/bin/env python

# Read - Eval - Print - Loop

import sys

# NOTE get environment variables list
# NOTE import built-ins and get list

def path_search_and_exec(command):
    pass


while True:
    command = input("$ ").split()
    # NOTE Default to os applications

    if command[0] in builtIns:
        pass
    else:
        sys.stdout.write(path_search_and_exec(command))
