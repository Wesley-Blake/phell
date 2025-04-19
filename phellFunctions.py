# Built-ins for phell
import os, subprocess, sys
from pathlib import Path


# Navigation
def cd(command: list) -> None:
    try:
        os.chdir(command)
    except:
        sys.stdout.write(f"{command[0] failed to cd")

def ls(command: list) -> list:
    return os.listdir(command)

def pwd() -> str:
    return os.getcwd()

# Files
def cat(command: list) -> str:
    # The func below returns a string but doesn't mean it is a real file.
    filePath: str = os.path.abspath(command[1])
    if os.path.isfile(filePath):
        try:
            with open(filePath, "r") as file:
                return file.read()
        except:
            return f"Failed to open file: {command[1]}"
    else:
        return f"No file found or not file: {command[1]}"

# Interaction
def echo(command: list) -> str:
    #NOTE expand on this to single and doubel quote later.
    return " ".join(command)

def type(command: list) -> str:
    pass
