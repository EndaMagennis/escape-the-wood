import os
import sys
from time import sleep
from colorama import Fore
import map
import player

# The main logo in ascii
LOGO = """
    ______
   / __________________ _____  ___
  / __/ / ___/ ___/ __ `/ __ \/ _ \/
 / /___(__  / /__/ /_/ / /_/ /  __/
/_____/____/\___/\__,_/ .___/\___/
                     /_/
           ________
          /_  __/ /   ___
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
    You have awoken in an abandoned cottage deep in the woods.
    You must try to explore and try to find items to help you escape.
    Each new area you enter will have items and hints to guide you.
    Be sure to search and read item descriptions.
    You will encounter enemies and you will only have one opportunity
    to avoid death. Pay attention to the descriptions.
    If you are ever stuck, type 'help' to remind yourself of what you can do.
    In all, there are 9 rooms to explore and 2 enemies to defeat.
    If you are so inclined, you could draw a map to help guide you.
    Good luck to you... What did you say your name was?

    """

ACTION_DESCRIPTIONS = {
    "SEARCH('SE')": "Gives you a selection of places to search for items",
    "MOVE('MO')": "Describes the paths you may take",
    "LOOK('LO')": "Give you a descrption of a chosen item in your inventory",
    "USE('US')": "Uses an item in your inventory",
    "DESCRIBE('DE')": "Describes the current room",
    "END GAME('EN')": "Quits the game",
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

    if input not in this_list:
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

        # Checks if room has been vistited
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
        print(Fore.GREEN + f"""
        Conrgatulations! You have finished this section of the game!
        """)
        sleep(2)
        print(Fore.GREEN + "To Be Continued!")
        sleep(2)
        clear_terminal()
        return True


def initialize_game():
    """
    Resets the player object and room objects.
    Runs the main logic for the game.
    """
    # # Turning off user inputs
    # os.system("stty -echo")
    # # Printing logo
    # print(Fore.CYAN + LOGO)
    # # Waiting 2 seconds
    # sleep(2)
    # # Clearing the terminal
    # clear_terminal()
    # # Typing the intro
    # for char in INTRO:
    #     sleep(0.02)
    #     sys.stdout.write(Fore.GREEN + char)
    #     sys.stdout.flush()
    # # Turning on user inputs
    # os.system("stty echo")
    # Initializing all rooms
    map.initialize_all_rooms()
    # Setting item_locations
    map.set_item_locations_for_each_room()
    # Initializing rooms and enemies lists
    check_for_win_state()
    # Inititalizing the player with default settings
    current_player = player.Player(
        "",
        [],
        map.generate_room_from_name("The Cottage")
        )
    # Calling the name player method
    current_player.name_player()
    # Calling the describe room method
    current_player.current_room.describe_room()
    # Calling the register inputs method
    current_player.register_user_inputs()
    # Finally, calls the restart_game funtion when loop ends
    restart_game()


def restart_game():
    """
    Function to prompt player to restart the game.
    If yes, calls to intialize the game.
    If no, returns
    """
    choice = input(Fore.WHITE + "Would you like to restart?: (Y/N)")
    if choice == "y" or choice == "Y":
        initialize_game()
    elif choice == "n" or choice == "N":
        print(Fore.GREEN + "Thanks for playing! See you again!")
        return
    else:
        print(Fore.RED + "That's not a valid choice! Try again!")
        restart_game()
