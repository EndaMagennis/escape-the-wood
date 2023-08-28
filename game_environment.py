from os import system, name
import map
from colorama import Fore
from time import sleep

ACTION_DESCRIPTIONS = {

    "SEARCH": "Gives you a selection of places to search for items",
    "MOVE": "Describes the paths you may take",
    "CHECK": "Tells you what's in your inventory",
    "LOOK": "Give you a descrption of a chosen item in your inventory",
    "USE": "Uses an item in your inventory",
    "DESCRIBE": "Describes the current room",
    "EXIT": "Quits the game",
}

def clear_terminal():
    """ Function which check the shell and uses the relevant clear command"""
    print(Fore.WHITE)
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

def check_for_win_state():
    """
    Function which creates a list of un-explored 
    rooms and a list of enemy encounters.
    Removes rooms and encounters as player completes them. 
    When both lists are empty, returns a value of True.
    """
    # Empty lists of rooms and enemies
    rooms_remaining = []
    enemies_remaining = []

    # Iterates through each room
    for room in map.all_rooms:
        # If the room has an encounter
        if room.has_encounter:
            # Appends room to enemies list
            enemies_remaining.append(room)
        # Appends all rooms to remaining rooms list
        rooms_remaining.append(room)

        # Checks if room has been vistited, which only updates if player sucessfully changes room
        if room.has_been_visited:
            rooms_remaining.remove(room)
            # Avoid raising error by checking if room exists in list
            if room in enemies_remaining:
                enemies_remaining.remove(room)

    print(f"Enemies remaining: {len(enemies_remaining)}")
    print(f"Rooms remaining: {len(rooms_remaining)}")

    # Check if both lists are empty        
    if len(rooms_remaining) == 0 and len(enemies_remaining) == 0:
        sleep(3)
        print("Conrgatulations! You have finished this section of the game!")
        sleep(2)
        print("To Be Continued!")
        sleep(2)
        return True
    
     

