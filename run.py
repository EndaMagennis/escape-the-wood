import player
import item
import room

# variable to store the intro of the game
intro = """\nYou have awoken in a ramshackel abode on the outskirts of a town.
You have no recollection of who you are or how you've gotten here.
A voice calls out to you, seemingly from nowhere.\n
'Ho, there weary traveller, you are here for the Challenge of Kings.
That you have awoken is a testament in itself.
Now piece yourself together. Who are you?'\n
Your head begins swimming; the past rushing to meet the present.
You suddenely remember yourself.\n"""

# instantiating the rooms of the game world
cottage = room.cottage
woods = room.woods
dark_woods = room.dark_woods
church = room.chruch
village_path = room.village_path

# instantiating the player
current_player = player.Player("", [], dark_woods, [])


def main():
    print(intro)
    print(cottage.linked_rooms)
    current_player.search(dark_woods, dark_woods.searchable_areas)


main()
