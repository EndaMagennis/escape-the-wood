import item
import room


class Player:
    """
    A class to instantiate a player object and hold
    information such as a current room, inventory,
    and name.
    """
  
    def __init__(self, name, inventory, current_room, actions, id):
        """
        Initialises an instance of the player
        """
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
        self.actions = actions
        self.id = id
  
    def register_user_inputs(self, room):
        game = True
        room = self.current_room
        areas = room.searchable_areas
        actions = [
            "move", "use", "pick up", "attack",
            "look", "equip", "fight", "exit", "search"
        ]
        while game:

            user_action = input("What would you like to do?\n")
            user_action.lower()

            for a in actions:
                if user_action == a:
                    if user_action == actions[-1]:
                        self.search(room, areas)
                    if str(user_action) == "exit":
                        print("Exiting")
                        game = False

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
            room = self.current_room
            areas = room.searchable_areas
            print(room.name, areas)
            place_to_look = input("Where would you like to search?:\n")
            for area in areas:
                if place_to_look == str(area):
                    print(f"you search the {str(area)}")
                    break
    
    def pick_up_item(self, new_item):
        """
        Method to update the player's inventory with a
        new item, determined by the room the player is in. 
        """
        # append a dictionary entry to the player's inventory
        print(f"You have picked up the {new_item}")
        self.inventory.update(new_item)
        pass

    def discard_item(self, item):
        self.inventory.pop(item)
        pass

    def use_item(self, item):
        pass

    def move_to_room(self, room):
        # code to write
        pass
