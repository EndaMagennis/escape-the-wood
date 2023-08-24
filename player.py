import map
from time import sleep
import os

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
            if input == "exit":
                return
            # Check that only numbers and letter and spaces are used
            if not input.isalnum() and input.isspace():
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

    def register_user_inputs(self, room):
        """ Records user inputs and calls the relevant methods """
        # Setting game to true for a continuous loop
        self.alive = True
        room = self.current_room
        areas = room.searchable_areas
        # a list of possible actions
        actions = [
            "SEARCH", "MOVE", "CHECK", 
            "LOOK", "USE", "DESCRIBE", "EXIT", 
        ]

        while self.alive:
            print(f"You can do any of the following things:\n")
            print(*actions, sep = ", ")
            print()
            user_action = input("What would you like to do?\n")

            if self.validate_input(
                user_action, 
                "That is not a valid action. Try again\n", 
                "That is not a valid action. Try again\n") == False:
                    continue
            # Removing case sensitivity and checking for valid actions
            user_action = user_action.upper()
            if user_action in actions:
                if user_action == actions[0]:
                    # Clearing the terminal
                    os.system('cls')
                    # Calling the search method
                    self.search(room, areas)
                elif user_action == actions[1]:
                    # Clearing the terminal
                    os.system('cls')
                    # Calling the move_to_room method
                    self.move_to_room(room, "")
                elif user_action == actions[2]:
                    # Clearing the terminal
                    os.system('cls')
                    # Calling the check_inventory method
                    self.check_inventory()
                elif user_action == actions[3]:
                    # Clearing the terminal
                    os.system('cls')
                    # Calling the look method
                    self.look(self.current_room)
                elif user_action == actions[4]:
                    # Clearing the terminal
                    os.system('cls')
                    # Calling the use_item method
                    self.use_item(self.inventory)
                elif user_action == actions[5]:
                    # Clearing the terminal
                    os.system('cls')
                    # Calling the describe_room method
                    room.describe_room()
                elif user_action == actions[6]:
                    print("Exiting")
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

    def search(self, room, areas):
        """ Prompts user to search areas based on current room."""
        room = self.current_room
        item_location = room.item_location
        areas = room.searchable_areas
        print(*room.searchable_areas, sep = ", ")
        # ask user where to look
        place_to_look = input("Where would you like to search?:\n")

        if place_to_look.lower() in str(areas):
            # give user feedback
            print(f"You search the {place_to_look}...")
            sleep(3)
            # checking if the user is searching the item_location
            if place_to_look == item_location and not room.item_found:
                item = room.inventory
                print(f"You found the {item}")
                room.item_found = True
                # Calling the pick_up_item method to add the item to inventory
                self.pick_up_item(item)
            else:
                print("You found nothing")
                # repeating the method
                # issue: the item_location is randomized each time
                self.search(self.current_room,
                            self.current_room.searchable_areas)
        elif place_to_look == "exit":
                return
        else:
            print("That is not an area. Try again")
            self.search(room, areas)

    def check_inventory(self):
        print(f"You are currently holding:\n {self.inventory}")

    def look(self, room):
        room = self.current_room
        room.describe_paths()

    def pick_up_item(self, new_item):
        """
        Method to update the player's inventory with a
        new item, determined by the room the player is in.
        """
        # append a dictionary entry to the player's inventory
        print(f"You have picked up the {new_item}")
        self.inventory.append(new_item)
        
    def discard_item(self, item):
        # removes item from inventory
        self.inventory.pop(item)
        print("As soon as the item hits the ground, it mysteriously vanishes")

    def use_item(self, inventory):
        """
        Method prompts player to choose an item from their inventory.
        If it exists, it will return the item.
        """
        if len(inventory) > 0:
            print(*inventory, sep= ", ")
            chosen_item = input("What would you like to use?:\n")
            if self.validate_input(
                chosen_item, 
                "Not a valid selection. Please try again!",
                "Not a valid selection. Please try again!",
                ) == False:
                self.use_item(self.inventory)
            
            chosen_item = chosen_item.lower()
            if chosen_item in self.inventory:
                print(f"You use the {chosen_item}")
                
            else:
                print("That's not in your inventory")
                self.use_item(self.inventory)
            
            return chosen_item
        else:
            print("You haven't got anything to use.")

    def move_to_room(self, current_room, direction):

        current_room = self.current_room
        # Describing the directional options to the user
        current_room.describe_paths()
        # Prompting the user for directional input
        direction = input(f"Which direction?\n")
        # Validatiing user input
        if self.validate_input(
            direction,
            "Sorry, that is not a valid direction",
            "Sorry, that is not a valid direction"
            ) == False:
            # Repeating method until valid input is given
            self.move_to_room(self.current_room, " ")

        direction = direction.lower()
        # referencing the current rooms posible paths
        links = current_room.linked_rooms
        # checking if the user has chosen a possible cardinal direction
        if direction in links:
            # Setting current_room as has_been_visted
            current_room.has_been_visited = True
            # Setting the new_name variable as the value stored in the in the links key 
            new_name = links[direction]
            # Calling the generate_room_from_name function to return the associated room object
            new_room = map.generate_room_from_name(new_name)
            if new_room.required_item in self.inventory or new_room.has_event:
                # Setting the player's current room to the new_room
                self.current_room = new_room
                # Describing the new room to the user
                new_room.describe_room()
                if new_room.has_event:
                    self.trigger_event(new_room, new_room.required_item, "")
            else:
                print("You cannot go that way... yet")
                return
        else:
            print("That is not a possible path.")
            self.move_to_room(self.current_room, " ")

    def trigger_event(self, room, required_item, outcome):
        room = self.current_room
        required_item = room.required_item
        used_item = self.use_item(self.inventory)

        if room.has_encounter:
            if used_item == required_item:
                print("You did it")
            else:
                print("You Died. Game Over")
                self.alive = False
        
       