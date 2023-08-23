import map

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
        """ Method to validate user input when prompted"""
        try:
            if input == "exit":
                return
            if not input.isalnum():
                raise TypeError
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
        game = True
        room = self.current_room
        areas = room.searchable_areas
        # a list of possible actions
        actions = [
            "MOVE", "CHECK", "ATTACK",
            "LOOK", "FIGHT", "EXIT", "SEARCH"
        ]

        while game:
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
            if user_action.upper() in actions:
                if user_action == "search":
                    # Calling the search method
                    self.search(room, areas)
                elif user_action == "move":
                    # calling the move_to_room method
                    self.move_to_room(room, "")
                elif user_action == "check":
                    # Calling the check_inventory method
                    self.check_inventory()
                elif user_action == "look":
                    # Calling the look method
                    self.look(self.current_room)
                elif user_action == "exit":
                    print("Exiting")
                    game = False
            else:
                print("That is not a valid choice. Try again.")

    def name_player(self):
        """
        Prompts user to give player a name.
        Validates user input and sets player name if valid.
        """

        # prompting user to give a name
        player_name = input("Enter your name:\n").capitalize()
        if self.validate_input(
            player_name, 
            "Please give a name consisting only of numbers or letters", 
            "Please give a name name between 2 to 22 letters in length"
            ) == False:
            self.name_player()

        # sets the player name for the instance of the player
        self.name = player_name
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
            print(f"you search the {place_to_look}")
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

    def use_item(self, item):
        pass

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

        # referencing the current rooms posible paths
        links = current_room.linked_rooms
        # checking if the user has chosen a possible cardinal direction
        if direction.lower() in links:
            # Setting the new_name variable as the value stored in the in the links key 
            new_name = links[direction]
            # Calling the generate_room_from_name function to return the associated room object
            new_room = map.generate_room_from_name(new_name)
            # Setting the player's current room to the new_room
            self.current_room = new_room
            # Describing the new room to the user
            new_room.describe_room()    
        else:
            print("Wah wah")
            self.move_to_room(self.current_room, " ")
