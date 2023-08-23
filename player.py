import item
import room


class Player:
    """
    A class to instantiate a player object and hold
    information such as a current room, inventory,
    and name.
    """

    def __init__(self, name, inventory, current_room, actions):
        """
        Initialises an instance of the player
        """
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
        self.actions = actions

    def register_user_inputs(self, room):
        """
        Records user inputs and calls the relevant methods.
        """
        # Setting game to true for a continuous loop
        game = True
        room = self.current_room
        areas = room.searchable_areas
        # a list of possible actions
        actions = [
            "move", "use", "pick up", "attack",
            "look", "equip", "fight", "exit", "search"
        ]

        while game:
            print(f"You can do any of the following things:\n {actions}")
            user_action = input("What would you like to do?\n")

            # validating user input. as this is repeted code, i'm considering
            # creating a fuction to validate all instances of inputs
            try:
                # check that user_action only uses alphabet characters
                if not user_action.isalpha():
                    raise TypeError

            except TypeError:
                # if there are characters outside of the alphabet
                print("""I have no way to interpert such intent.
                Please use one of the following commands:\n""")

                print(actions)
                # repeat the method
                self.register_user_inputs(room)

            # ensuring that case sensitivity is not an issue
            # and that the action is possible
            if user_action.lower() in actions:
                if user_action == "search":
                    self.search(room, areas)
                elif user_action == "move":
                    self.move_to_room(room, "")
                elif str(user_action) == "exit":
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
        player_name = input("Enter your name:\n")
        # sets the player name for the instance of the player
        self.name = player_name
        try:
            # check that player_name only uses alphabet characters
            if not player_name.isalpha():
                raise TypeError
            # check that the player_name is within the charcter limit
            elif len(player_name) < 3 or len(player_name) > 12:
                raise ValueError
            print(f"Welcome, {player_name}. Your journey begins here.")

        except TypeError:
            # if there are characters outside of the alphabet
            print("""How could ones name consist of anything but letters?
            Surely you lie!\n""")
            self.name_player()

        except ValueError:
            # if the player name is outside the character limit
            print(f"""I find it hard to believe that your
            name is {len(player_name)} letters long.
            Most names are longer than 3 letters
            and shorter than 12. Try again.\n""")
            self.name_player()
        return player_name

    def search(self, room, areas):
        """
        Prompts user to search areas based on current room.
        """
        room = self.current_room
        areas = room.searchable_areas
        item_location = room.choose_random_item_location(
                        room.searchable_areas)
        print(item_location)
        # ask user where to look
        place_to_look = input("Where would you like to search?:\n")

        for area in areas:
            # check that player has put in searchable area
            if place_to_look == str(area):
                # give user feedback
                print(f"you search the {str(area)}")
                # checking if the user is searching the item_location
                if place_to_look == item_location:
                    print(f"You found the {room.inventory}")
                    # adding the item to inventory
                    self.pick_up_item(room.inventory)
                else:
                    print("You found nothing")
                    # repeating the method
                    # issue: the item_location is randomized each time
                    self.search(self.current_room,
                                self.current_room.searchable_areas)
            else:
                print("That is not an area. Try again")
                self.search(room, areas)

    def pick_up_item(self, new_item):
        """
        Method to update the player's inventory with a
        new item, determined by the room the player is in.
        """
        # append a dictionary entry to the player's inventory
        print(f"You have picked up the {new_item}")
        for id, key in new_item:
            print(id)
            return key, id

    def discard_item(self, item):
        # removes item from inventory
        self.inventory.pop(item)
        print("As soon as the item hits the ground, it mysteriously vanishes")

    def use_item(self, item):
        pass

    def move_to_room(self, current_room, direction):

        current_room = self.current_room
        direction = input(f"Which direction?\n")
        links = current_room.linked_rooms
        # checking if the user has chosen a possible cardinal direction
        if direction in links:
            print(links.keys())
