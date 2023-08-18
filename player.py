class Player:
    """
    A class to instantiate a player object and hold
    information such as a current room, inventory,
    and name.
    """
    def __init__(self, name, inventory, current_room, actions, id):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room
        self.actions = actions
        self.id = id

    def name_player(self):
        """
        Prompts user to give player a name.
        Validates user input and sets player name if valid.
        """
        player_name = input("Enter your name:\n")
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
            print(f"""I find it hard to believe that your
            name is {len(player_name)} letters long.
            Most names are longer than 3 letters
            and shorter than 12. Try again.\n""")
            self.name_player()
        return player_name

    def pick_up_item(self):
        # code to write
        pass

    def use_item(self, item):
        # code to write
        pass

    def move_to_room(self, room):
        # code to write
        pass
