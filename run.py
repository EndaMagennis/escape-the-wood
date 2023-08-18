# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import player
import input_handler


intro = """\nYou have awoken in a ramshackel abode on the outskirts of a town.
You have no recollection of who you are or how you've gotten here.
A voice calls out to you, seemingly from nowhere.\n
'Ho, there weary traveller, you are here for the Challenge of Kings.
That you have awoken is a testament in itself.
Now piece yourself together. Who are you?'\n
Your head begins swimming; the past rushing to meet the present.
You suddenely remember yourself.\n"""

current_player = player.Player("", [], (0, 0), {}, 1)
iph = input_handler.InputHandler()


def main():
    print(intro)
    current_player.name_player()
    iph.register_user_inputs()


main()
