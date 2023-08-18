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

        player_name = input("Enter your name:\n")
        self.name = player_name
        try:
            if not player_name.isalpha():
                raise TypeError
            elif len(player_name) < 3:
                raise ValueError
            print(f"Welcome, {player_name}. Your journey begins here.")

        except TypeError:
            print("""How could ones name consist of anything but letters?
Surely you lie!\n""")
            self.name_player()

        except ValueError:
            print("""Drawing a blank are we? Come now, what is your full name?
Only titles have fewer than 3 letters\n""")
            self.name_player()
        return player_name
