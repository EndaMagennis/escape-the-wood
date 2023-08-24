import player
import map
import sys
import os
from time import sleep

# The main logo in ascii
logo ="""
    ______                              ________            _       __                __    
   / ____/_____________ _____  ___     /_  __/ /_  ___     | |     / /___  ____  ____/ /____
  / __/ / ___/ ___/ __ `/ __ \/ _ \     / / / __ \/ _ \    | | /| / / __ \/ __ \/ __  / ___/
 / /___(__  ) /__/ /_/ / /_/ /  __/    / / / / / /  __/    | |/ |/ / /_/ / /_/ / /_/ (__  ) 
/_____/____/\___/\__,_/ .___/\___/    /_/ /_/ /_/\___/     |__/|__/\____/\____/\__,_/____/  
                     /_/                                                                    

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
    os.system('cls')

    for char in intro:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

    map.set_item_locations_for_each_room()
    current_player.name_player()
    current_player.current_room.describe_room()
    current_player.register_user_inputs(current_player.current_room)


main()
