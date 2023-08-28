import map
import game_environment
import item
from time import sleep
from colorama import Fore

class Player():
    """
    A class to instantiate a player object and hold
    information such as a current room, inventory,
    and name.
    """

    def __init__(self, name, inventory, current_room):
        """ Initialises an instance of the player """
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
    
    def validate_input(self, input, type_err_message, val_err_message):
        """
        Method to validate user input when prompted.
        Will raise a Type Error or Value Error for invalid inputs.
        Prints a message relevant to error type.
        """
        try:
            # Check if user enters exit at any input phase
            if input == "exit" or input == "EXIT":
                return
            # Check that only numbers and letter and spaces are used
            if not input.isalnum() and not input.isspace():
                raise TypeError
            # Control the length of the input
            elif len(input) < 2 or len(input) > 22:
                raise ValueError
        
        except TypeError:
            print(type_err_message)
            return False
        
        except ValueError:
            print(val_err_message)
            return False
        return True

    def register_user_inputs(self):
        """ Records user inputs and calls the relevant methods """
        # Setting self.alive to true for a continuous loop
        self.alive = True
        if game_environment.check_for_win_state() == True:
            self.alive = False
        room = self.current_room
        # A list of possible actions
        actions = [
            "SEARCH", "MOVE", "CHECK", 
            "LOOK", "USE", "DESCRIBE", "EXIT", "HELP"
        ]
        # Running a continuous loop
        while self.alive:
            print(f"You can do any of the following things:")
            print(Fore.BLUE)
            print(*actions, sep = ", ")
            print(Fore.WHITE)

            # Promting user for input
            user_action = input("What would you like to do?\n")
            # Validatong user input
            if self.validate_input(
                user_action, 
                f"Not quite sure what you mean by {user_action}, use your words!\n", 
                "Give me at least the first two letters of your intention, for Pete's sake!\n") == False:
                    continue
            # Removing case sensitivity and checking for valid actions
            user_action = user_action.upper()
            # Checking if user_action partially matches the action
            if user_action in actions[0]:
                # Calling the search method
                self.search(self.current_room)

            elif user_action in actions[1]:
                # Calling the move_to_room method
                self.move_to_room(room)

            elif user_action in actions[2]:
                # Calling the check_inventory method
                self.check_inventory()

            elif user_action in actions[3]:
                # Calling the look method
                self.look(self.inventory)

            elif user_action in actions[4]:
                # Calling the use_item method
                self.use_item(self.inventory)

            elif user_action in actions[5]:
                # Calling the describe_room method
                self.current_room.describe_room()

            elif user_action in actions[6]:
                print("Exiting")
                # Ending the loop
                self.alive = False

            elif user_action in actions[7]:
                # Calling the describe_room method
                self.help()

            else:
                print("That is not a valid choice. Try again.")

    def name_player(self):
        """
        Prompts user to give player a name.
        Validates user input and sets player name if valid.
        """

        # Prompting user to give a name
        player_name = input(Fore.WHITE + "Enter your name:\n").capitalize()
        # Calling the validate_input method to validate player_name
        if self.validate_input(
            player_name, 
            "Please give a name consisting only of numbers or letters", 
            "Please give a name name between 2 to 22 letters in length"
            ) == False:
            # Repeating the name_player method until a valid input is given.
            self.name_player()
        else:
        # If the input is valid
            self.name = player_name
            print(f"Hello, {player_name}. Your journey begins in:\n")
            return player_name

    def help(self):
        for x in game_environment.ACTION_DESCRIPTIONS.keys():
            print(f"{Fore.BLUE + x}: {Fore.WHITE + game_environment.ACTION_DESCRIPTIONS[x]}")

    def search(self, room):
        """ Prompts user to search areas based on current room."""
        # First clears the terminal
        game_environment.clear_terminal()

        # Set room variable to current room
        room = self.current_room

        # Set possible areas to this room's searchable areas
        possible_areas = room.searchable_areas

        # set the item_location
        item_location = room.item_location

        # Give the user the list of searchable areas
        print("These seem like worthy locations:\n")
        for area in possible_areas:
            print(Fore.GREEN + area)

        # Prompt user to choose from the list    
        player_choice = input(Fore.WHITE + "Where would you like to search?:\n")

        # Validate user input
        if self.validate_input(
            player_choice,
            f"Surely you understand that it is impossible to search a {player_choice}. Try using letters.",
            "I need at least 2 letters to understand where you're looking."
            ) == False:
            return

        # If valid set to uppercase to match against searchable areas
        player_choice = player_choice.upper()

        # Set variable to returned value of check for partial match function
        outcome = game_environment.check_for_partial_match(
            player_choice, 
            possible_areas, 
            area, 
            f"Surely you know {player_choice} isn't a choice?"
            )
        
        # Check if outcome is in possible areas
        if outcome in possible_areas:
            # Set player choice to the full string
            player_choice = outcome
            # Give user feedback
            print(f"You search the {Fore.GREEN + player_choice}")
            # Change back to white color
            print(Fore.WHITE)
            sleep(2)

            # Check if user has found the item and making sure item has not been foun already
            if player_choice == item_location and room.item_found == False and not room.has_event:
                # Setting the item_found to True for this room
                room.item_found = True
                # Give user feedback
                print(f"You found the {Fore.MAGENTA + room.inventory.upper()}")
                sleep(2)
                # Call the pick_up_item method and setting the inventory to uppercase
                self.pick_up_item(room.inventory.upper())
            # Checking if room has event
            elif room.has_event:
                print("You cannot open it. Come back and try again.")
            else:
                print(f"You found nothing")
                sleep(2)
                # Repeats the method
                self.search(room)
            
    def check_inventory(self):
        # First clears the terminal
        game_environment.clear_terminal()
        # Prints inventory in magenta and resets to white
        print("You are currently holding: ")
        print(Fore.MAGENTA)
        print(*self.inventory, sep= ",  ")
        print(Fore.WHITE)

    def look(self, inventory):
        """A method which prints the chosen item description if player has item in inventory"""
        # First clears the terminal
        game_environment.clear_terminal()
        # Check that there is something in the inventory
        if len(inventory) > 0:
            # Print the inventory
            print("What would you like to look at?\n")
            print(Fore.MAGENTA)
            print(*inventory, sep= ", ")
            # Prompt user to choose an item
            chosen_item = input(Fore.WHITE + "\n")
            # Validate user input
            if self.validate_input(
                chosen_item,
                f"It's impossible to hold a {chosen_item}. Try words.",
                "I need at least 2 letters of what you're looking for."
            ) == False: 
                return
            else:
                chosen_item = chosen_item.upper()
                for this_item in inventory:
                    if chosen_item in this_item:
                        chosen_item = this_item
                        chosen_item = chosen_item.lower()
                        outcome = item.return_item_description(chosen_item)
                        print(f"{Fore.MAGENTA + chosen_item.upper()}\n{Fore.WHITE + outcome.capitalize()}\n")
                        sleep(2)
                    else:
                        continue
                if chosen_item.upper() not in inventory:
                    print("Haven't got that.")
        else:
            print("You haven't got anything")

    def pick_up_item(self, new_item):
        """
        Method to update the player's inventory with a
        new item, determined by the room the player is in.
        """
        # First clears the terminal
        game_environment.clear_terminal()
        # append a dictionary entry to the player's inventory
        print(f"You have picked up the {Fore.MAGENTA + new_item}\n")
        self.inventory.append(new_item)
        print(Fore.WHITE)

    def use_item(self, inventory):
        """
        Method prompts player to choose an item from their inventory.
        If it exists, it will return the item.
        """
        if len(inventory) > 0:

            current_room = self.current_room
            print("You're currently holding:")
            print(Fore.MAGENTA)
            print(*inventory, sep= ", ")
            print(Fore.WHITE)
            chosen_item = input("What would you like to use?:\n")
            # Validating user input
            if self.validate_input(
                chosen_item, 
                f"It's hard to carry a {chosen_item}, perhaps try something real!",
                f"I need more that {len(chosen_item)} to work with. Give me at least 3 letters",
                ) == False:
                return
            # If valid
            chosen_item = chosen_item.upper()
            for x in self.inventory:
                if chosen_item in x:
                    chosen_item = x
                    print(f"You use the {Fore.MAGENTA + x}")
                    if (current_room.name == "The Cottage" or current_room.name == "The Village") and chosen_item == current_room.required_item.upper():
                        sleep(2)
                        print(Fore.WHITE + "You hear a *click* as the key turns in the lock")
                    print(Fore.WHITE)
                    # Set partial choice to full choice
                    return chosen_item
                elif chosen_item == "EXIT":
                    return
                else:
                    continue
            if chosen_item not in self.inventory:
                print("You haven't got that. Try again.")
                self.use_item(self.inventory)
                
        else:
            print("You haven't got anything to use.\n")

    def move_to_room(self, current_room):
        # First clears the terminal
        game_environment.clear_terminal()

        current_room = self.current_room
        # Describing the directional options to the user
        current_room.describe_paths()
        # Prompting the user for directional input
        direction = input(f"Which direction?\n")
        # Validatiing user input
        if self.validate_input(
            direction,
            "Sorry, that is not a valid direction\n",
            "Sorry, that is not a valid direction\n"
            ) == False:
            # Repeating method until valid input is given
            return

        direction = direction.lower()
        if direction == "exit":
            return
        # referencing the current rooms posible paths
        links = current_room.linked_rooms

        for link in links:
            # checking if the user has entered a full or partial string for direction
            if direction in link:
                direction = link
                # Setting current_room as has_been_visted
                current_room.has_been_visited = True
                # Setting the new_name variable as the value stored in the in the links key 
                new_name = links[direction]
                # Calling the generate_room_from_name function to return the associated room object
                new_room = map.generate_room_from_name(new_name)
                # Checking if user has the required item to move on
                if new_room.required_item.upper() in self.inventory or new_room.has_event:
                    # Setting the player's current room to the new_room
                    self.current_room = new_room
                    # Describing the new room to the user
                    print(f"You have chosen to go {Fore.CYAN + direction.upper()}...")
                    sleep(3)
                    # Clearing the terminal
                    game_environment.clear_terminal()

                    # Checking if new room is The Dark Woods
                    if new_room.name == "The Dark Woods" and not new_room.has_been_visited:
                        # Changing the has_event of the dark wood
                        new_room.has_event = True
                        # Changing the required item for the encounter
                        new_room.required_item = "mace"

                    new_room.describe_room()
                    
                    if new_room.has_event:
                        sleep(2)
                        self.trigger_event()

                    game_environment.check_for_win_state()

                else:
                    print(f"You cannot go that way... yet\n")
                    return
            else:
                continue
        if not direction in links:
            print(f"You and I both know that {direction} is not a direction")
            sleep(2)

    def trigger_event(self):
        room = self.current_room
        required_item = room.required_item
        used_item = self.use_item(self.inventory)
        print(used_item)
        # Check for an encounter
        if room.has_encounter:
            if used_item == required_item.upper():
                print("...")
                sleep(2)
                print("You bested the beast!")
                room.has_encounter = False
                room.has_event = False
            else:
                print("...")
                sleep(2)
                print("You Died. Game Over\n")
                self.alive = False
        else:
            if used_item == required_item.upper():
                print("...")
                sleep(2)
                print("You did it\n")
                room.has_encounter = False
                room.has_event = False
            else:
                print("...")
                sleep(2)
                print("It did not work\n")
        
# Instantiating the player with no name, with no inventory, in the Cottage
current_player = Player("", [], map.generate_room_from_name("The Cottage"))
