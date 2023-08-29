import os
import sys
from time import sleep
from colorama import Fore
import map
import player

# The main logo in ascii
LOGO ="""
    ______                         
   / __________________ _____  ___ 
  / __/ / ___/ ___/ __ `/ __ \/ _ \/
 / /___(__  / /__/ /_/ / /_/ /  __/
/_____/____/\___/\__,_/ .___/\___/ 
                     /_/           
           ________       
          /_  __/ /_  ___ 
           / / / __ \/ _ \/
          / / / / / /  __/
         /_/ /_/ /_/\___/ 
 _       __                __    
| |     / ____  ____  ____/ _____
| | /| / / __ \/ __ \/ __  / ___/
| |/ |/ / /_/ / /_/ / /_/ (__  ) 
|__/|__/\____/\____/\__,_/____/  

"""

# Variable to store the intro of the game
INTRO = f"""
    You have awoken in a ramshackel abode on the outskirts of a town.
    You have no recollection of who you are or how you've gotten here.
    A voice calls out to you, seemingly from nowhere.
    
        'Ho, there weary traveller, you are here for the Challenge of Kings.
    That you have awoken is a testament in itself.
    Now piece yourself together. Who are you?'

    Your head begins swimming; the past rushing to meet the present.
    You suddenely remember yourself.
    """

ACTION_DESCRIPTIONS = {
    "SEARCH": "Gives you a selection of places to search for items",
    "MOVE": "Describes the paths you may take",
    "LOOK": "Give you a descrption of a chosen item in your inventory",
    "USE": "Uses an item in your inventory",
    "DESCRIBE": "Describes the current room",
    "END GAME": "Quits the game",
}

def clear_terminal():
    """ Function which check the shell and uses the relevant clear command"""
    print(Fore.WHITE)
    # Check if operating system name is Windows
    if os.name == 'nt':
        command = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        command = os.system('clear')

def check_for_partial_match(input, this_list, list_item, negative_statement):
    """
    Iterates through a list and checks if the 
    input value is a partial match for an item in the list
    """
    for list_item in this_list:
        if input in list_item:
            return list_item
        elif input == "exit" or input == "EXIT":
            return
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
        print(Fore.GREEN + "Conrgatulations! You have finished this section of the game!")
        sleep(2)
        print(Fore.GREEN + "To Be Continued!")
        sleep(2)
        clear_terminal()
        return True

def initialize_game():
    # Turning off user inputs
    os.system("stty -echo")
    # Printing logo
    print(Fore.CYAN + LOGO)
    # Waiting 2 seconds
    sleep(2)
    # Clearing the terminal
    clear_terminal()
    # Typing the intro
    for char in INTRO:
        sleep(0.02)
        sys.stdout.write(Fore.GREEN + char)
        sys.stdout.flush()
    # Turning on user inputs
    os.system("stty echo")
    # Initializing all rooms
    map.initialize_all_rooms()
    # Setting item_locations
    map.set_item_locations_for_each_room()
    # Initializing rooms and enemies lists
    check_for_win_state()
    # Inititalizing the player with default settings
    current_player = player.Player("", [], map.generate_room_from_name("The Cottage"))
    #
    current_player.name_player()
    #
    current_player.current_room.describe_room()
    # 
    current_player.register_user_inputs()
    #
    restart_game()

def restart_game():
    choice = input(Fore.WHITE + "Would you like to restart?: (Y/N)")
    if choice == "y" or choice == "Y":
        initialize_game()
    elif choice == "n" or choice == "N":
        print(Fore.GREEN + "Thanks for playing! See you again!")
        return
    else:
        print(Fore.RED + "That's not a valid choice! Try again!")
        restart_game()