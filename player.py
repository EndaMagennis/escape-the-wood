import map
import game_environment
from time import sleep

class Player:
    """
    A class to instantiate a player object and hold
    information such as a current room, inventory,
    and name.
    """

    def __init__(self, name, inventory, current_room, actions):
        """ Initialises an instance of the player """
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
        self.actions = actions
    
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
        room = self.current_room
        # A list of possible actions
        actions = [
            "SEARCH", "MOVE", "CHECK", 
            "LOOK", "USE", "DESCRIBE", "EXIT", 
        ]
        # Running a continuous loop
        while self.alive:
            print(f"You can do any of the following things:\n")
            print(*actions, sep = ", ")
            print()

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
                self.look()

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
            else:
                print("That is not a valid choice. Try again.")

    def name_player(self):
        """
        Prompts user to give player a name.
        Validates user input and sets player name if valid.
        """

        # Prompting user to give a name
        player_name = input("Enter your name:\n").capitalize()
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
            print(f"Hello, {player_name}. Your journey begins in: ")
            return player_name

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
            print(area)

        # Prompt user to choose from the list    
        player_choice = input("Where would you like to search?:\n")

        # Validate user input
        if self.validate_input(
            player_choice,
            f"Surely you understand that it is impossible to search a {player_choice}. Try using letters.",
            "I need at least 2 letters to understand where you're looking."
            ) == False:
            self.search()

        # If valid set to uppercase to match against searchable areas
        player_choice = player_choice.upper()

        # Cycle through each area
        for x in possible_areas:
            # Check for a partial string match of the area
            if player_choice in x:
                # Set player_choice to the full string
                player_choice = x
                # Give user feedback
                print(f"You search the {x}")
                sleep(2)
                # Check if player has found the item and if item has not been found
                if player_choice == item_location and room.item_found == False:
                    # Set room.item_found to True
                    room.item_found = True
                    # Give user feedback
                    print(f"You found the {room.inventory.upper()}")
                    sleep(2)
                    # Call the pick_up_item method
                    self.pick_up_item(room.inventory.upper())
                else:
                    print(f"You found nothing")
                    sleep(2)
                    # Repeats the method
                    self.search(room)
            elif player_choice == "EXIT":
                return
            else:
                # Continuing cycle until a match is found
                continue
        if not player_choice in possible_areas:
                print("You must be confused. Thats not a valid choice")
                sleep(2)
            
    def check_inventory(self):
        # First clears the terminal
        game_environment.clear_terminal()

        print(f"You are currently holding:\n {self.inventory}\n")

    def look(self):
        # First clears the terminal
        game_environment.clear_terminal()

        pass

    def pick_up_item(self, new_item):
        """
        Method to update the player's inventory with a
        new item, determined by the room the player is in.
        """
        # First clears the terminal
        game_environment.clear_terminal()

        # append a dictionary entry to the player's inventory
        print(f"You have picked up the {new_item}\n")
        self.inventory.append(new_item)

    def use_item(self, inventory):
        """
        Method prompts player to choose an item from their inventory.
        If it exists, it will return the item.
        """
        # First clears the terminal
        game_environment.clear_terminal()

        if len(inventory) > 0:
            print("You're currently holding:\n")
            print(*inventory, sep= ", ")
            chosen_item = input("What would you like to use?:\n")
            # Validating user input
            if self.validate_input(
                chosen_item, 
                f"It's hard to carry a {chosen_item}, perhaps try something real!",
                f"I need more that {len(chosen_item)} to work with. Give me at least 3 letters",
                ) == False:
                return
            else:
                # If valid
                chosen_item = chosen_item.upper()
                for x in self.inventory:
                    continue
                if chosen_item in x:
                    print(f"You use the {x}")
                elif chosen_item == "EXIT":
                    return
                else:
                    print("That's not in your inventory\n")
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
            self.move_to_room(self.current_room, direction)

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
                    print(f"You have chosen to go {direction.upper()}...")
                    sleep(3)
                    game_environment.clear_terminal()
                    new_room.describe_room()
                    if new_room.has_event:
                        self.trigger_event(new_room, new_room.required_item)
                else:
                    print(f"You cannot go that way... yet\n")
                    return
            else:
                continue
        if not direction in links:
            print(f"You and I both know that {direction} is not a direction")
            sleep(2)

    def trigger_event(self, room, required_item):
        room = self.current_room
        required_item = room.required_item
        used_item = self.use_item(self.inventory)
        used_item = used_item.upper()
        # Check for an encounter
        if room.has_encounter:
            if used_item == required_item.upper():
                print("...")
                sleep(2)
                print("You did it\n")
                room.has_encounter = False
                room.has_event = False
            else:
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
                self.trigger_event(room, required_item)
        
       