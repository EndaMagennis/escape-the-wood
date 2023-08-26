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

def check_for_partial_match(input, this_list, list_item, negative_statement):

    for list_item in this_list:
        if input in list_item:
            return list_item
        else:
            continue
    
    if not input in this_list:
        print(negative_statement)
        return
