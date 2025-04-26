# Built-ins for phell
import os
from pathlib import Path


# Navigation
def pwd() -> str:
    sys.stdout.write(os.getcwd()+"\n")

def cd(command: list) -> None:
    try:
        os.chdir(" ".join(command[1:]))
    except Exception as e:
        sys.stdout.write(str(e)+"\n")

def ls(command: list) -> None:
    try:
        sys.stdout.write("\n".join(os.listdir())+"\n")
    except Exception as e:
        sys.stdout.write(str(e)+"\n")


# Interaction
def echo(command: list) -> str:
    #NOTE expand on this to single and doubel quote later.
    sys.stdout.write(" ".join(command)+"\n")

def type(command: list) -> None:
    if command[0] in builtIns:
        sys.stdout.write(f"{command[0]} is a built in")
    else:
        #NOTE search PATH
        pass


# Files
def cat(command: list) -> None:
    # The func below returns a string but doesn't mean it is a real file.
    filePath: str = os.path.abspath(command[1])
    if os.path.isfile(filePath):
        try:
            with open(filePath, "r") as file:
                sys.stdout.write(file.read())
        except:
            sys.stdout.write(f"Failed to open file: {command[1]}")
    else:
        sys.stdout.write(f"No file found or not file: {command[1]}")
