class InputHandler():
    """
    Handles user inputs and carries out relevant methods
    """
    def __init__(self):
        pass

    def register_user_inputs(self, player):
        game = True
        actions = [
            "move", "use", "pick up", "attack",
            "look", "equip", "fight", "exit"
        ]
        while game:

            user_action = input("What would you like to do?\n")

            for a in actions:
                if str(a) == str(user_action):
                    if str(user_action) == str(actions[-1]):
                        print("Exiting")
                        game = False
