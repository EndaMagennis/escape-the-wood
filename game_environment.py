from os import system, name

class GameEnvironment:
    """
    Handles game state to allow for save/load functionality
    """


def clear_terminal():
    """ Function which check the shell and uses the relevant clear command"""
    # Check if operating system name is Windows
    if name == 'nt':
        command = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        command = system('clear')