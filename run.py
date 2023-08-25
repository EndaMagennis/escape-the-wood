import player
import map
import sys
import game_environment
from time import sleep

# The main logo in ascii
logo ="""
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
intro = f"""
    You have awoken in a ramshackel abode on the outskirts of a town.
    You have no recollection of who you are or how you've gotten here.
    A voice calls out to you, seemingly from nowhere.
    
        'Ho, there weary traveller, you are here for the Challenge of Kings.
    That you have awoken is a testament in itself.
    Now piece yourself together. Who are you?'

    Your head begins swimming; the past rushing to meet the present.
    You suddenely remember yourself.
    """

# Instantiating the player
current_player = player.Player("", [], map.generate_room_from_name("The Cottage"), [])


def main():

    print(logo)
    sleep(2)
    game_environment.clear_terminal()

    for char in intro:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

    map.set_item_locations_for_each_room()
    current_player.name_player()
    current_player.current_room.describe_room()
    current_player.register_user_inputs()


main()
