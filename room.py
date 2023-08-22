import item
import random


class Room:
    """
    Creates an instance of the Room class.
    """
    def __init__(
                self, name, description, path_descriptions, inventory,
                searchable_areas, item_location, linked_rooms, required_item
                ):
        self.name = name
        self.description = description
        self.path_descriptions = path_descriptions
        self.inventory = inventory
        self.searchable_areas = searchable_areas
        self.item_location = item_location
        self.linked_rooms = linked_rooms
        self.required_item = required_item

    def describe_room(self):
        """
        Describes the instance of a room.
        """
        print(self.description)
    
    def describe_paths(self):
        """
        Describes the North, South, East and West paths from current room
        """
        print(self.path_descriptions)

    def choose_random_item_location(self, searchable_areas):
        """
        Randomly selects which of the searchable areas holds the item
        """
        searchable_areas = self.searchable_areas
        random_choice = random.randint(0, len(searchable_areas) - 1)  
        selected_area = searchable_areas[random_choice]

        self.item_location = selected_area
        return selected_area


# creating a 'cottage' room instance
cottage = Room(
    "The Cottage",
    """
     A small, rustic, thach rooved house.
    It's barren interior only hinting at a life which once resided within.
    In the western corner of the room you see a bookshelf.
    in the center of the room there is a large bed.
    Next to the bed, there is a cabinet
    """,
    """
    Outside, north of you, appears to be a woodland.
    However, the door appears to be locked.
    """,
    item.return_item("cottage key"), ["bookshelf", "cabinet", "bed"], "",
    {"north": "woods"}, ""
    )

woods = Room(
    "The Woods",
    """
    A dark and damp wood engulfs the path before you.
    Barely a speck of sunlight can be seen. Dark shadows in your perifery dance
    and move. Your eyes struggle to focus. Your legs carry you forward, like
    some sort of wretched automoton. Soon, you find a small clearing.""",

    """
    To the North, is an overgrown path which weaves,
    seemingly endlessly, into the abyss of the woods.
    South leads back to the cottage.
    To the East, a path darker still than that which you have come.
    To your West lies a thicket of sharp brambles.
    """,
    item.return_item("broken sword"), ["brambles"], "",
    {"north": "village path", "south": "cottage",
        "east": "dark woods", "west": "glade"}, "cottage key"
)

village_path = Room(
    "The Village Path",
    """
    This winding path meanders back and forth,
    stitching itself through the trees. As you toil your way through
    you feel your legs ache. You can't say how long you've been walking.
    Finally, mercifully, you see before you a spire of a church.
    You pasue and take a breather. You notice a formation of leaves nearby.
    There also seems to be a faint shimmer by a nearby tree.
    """,

    """North of you is the church spire, jutting out above the canopy.
    South leads back to the woods.
    East, you can hear the gentle trickle of water.
    West of you the path disappears, yet again, into a thick, black void.
    """,
    item.return_item("rusted key"), ["leaf pile", "nearby tree"], "",
    {"north": "church", "south": "woods",
        "east": "river", "west": "dark wood"}, ""
)

chruch = Room(
    "The Abandoned Church",
    """
    You are awestruck by the sheer scale of this building. Your awe and wonder
    soon turn to worry as you notice the decay and decimation which has
    befallen the sanctuary. The door is all but rotted away and with a
    gentle push, it leaves its hinges, flopping to the floor before you.
    Its vast, cavernous halls amplify the wind, invoking a thunderous bellow.
    The pulpit still stands just off-centered, giving way to the vast
    table of worship. Behind the table, the unmistakable shimmer of
    the tabernacle glistens.
    """,

    """
    South leads back to the village path.
    East of the chuch the path continues,
    though little can be seen of a village.
    West of the church is a clearing of some sort.
    """,
    item.return_item("book"), ["pulpit", "tabernacle", "table"], "",
    {"south": "village path", "east": "village", "west": "clearing"}, ""
)
