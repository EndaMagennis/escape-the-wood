# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from player import Player

intro = """\nYou have awoken in a ramshackel abode on the outskirts of a town.
You have no recollection of who you are or how you've gotten here.
A voice calls out to you, seemingly from nowhere.\n
'Ho, there weary traveller, you are here for the Challenge of Kings.
That you have awoken is a testament in itself.
Now piece yourself together. Who are you?'\n
Your head begins swimming; the past rushing to meet the present.
You suddenely remember yourself.\n"""
player = Player("", [], (0, 0), [], 1)


def main():
    print(intro)
    player.name_player()


main()
