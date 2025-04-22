# /usr/bin/env python

import subprocess
import phellFunctions

# NOTE get environment variables list
builtIns = []
for functions in dir(phellFunctions):
    if "__" not in functions:
        builtIns.append(functions)


while True:
    command = input("$ ").split()
    if not command: continue
    # NOTE Default to os applications

    if command[0] in builtIns:
        match command[0]:
            # Navigation
            case "cd":
                pass
            case "ls":
                pass
            case "pwd":
                pass

            # Files
            case "cat":
                pass

            # Interaction
            case "echo":
                pass
            case "type":
                pass
    elif command[0] == "exit": exit()
    else:
        subprocess.run(command)
