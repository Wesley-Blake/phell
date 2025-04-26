# /usr/bin/env python

import sys, subprocess, phellFunctions

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
                phellFunctions.cd(command)
            case "ls":
                phellFunctions.ls(command)
            case "pwd":
                phellFunctions.pwd()

            # Interaction
            case "echo":
                phellFunctions.echo(command)
            case "type":
                pass

            # Files
            case "cat":
                pass

    elif command[0] == "exit": exit()
    else:
        try:
            subprocess.run(command)
        except Exception as e:
            sys.stdout.write(f"{command[0]} isn't in PATH")
