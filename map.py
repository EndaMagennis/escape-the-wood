import room
import item

"""
This script holds the instances of each room.
Originally, they were in the room.py script,
but for readability it was decided that they should
be in a separate file.
"""
# Creating a cottage Room
cottage = room.Room(
    # Room name
    "The Cottage",
    # Room decription
    """
    A small, rustic, thach rooved house.
    It's barren interior only hinting at a life which once resided within.
    In the western corner of the room you see a bookshelf.
    in the center of the room there is a large bed.
    Next to the bed, there is a cabinet
    """,
    # Path description; tells user which directions are possible
    """
    Outside, north of you, appears to be a woodland.
    However, the door appears to be locked.
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("cottage key"),
    # List of searchable areas 
    ["bookshelf", "cabinet", "bed"],
    # Where the item can be found 
    "bookshelf",
    # Links to other rooms
    {"north": "The Woods"},
    # Items required to enter this room 
    None
    )

# Creating a cottage Room
woods = room.Room(
    # Room name
    "The Woods",
    # Room decription
    f"""
    A dark and damp wood engulfs the path before you.
    Barely a speck of sunlight can be seen. Dark shadows in your perifery dance
    and move. Your eyes struggle to focus. Your legs carry you forward, like
    some sort of wretched automoton. Soon, you come to a fork in the woods.
    A thick net of brambles seems to conceal a glimmer.
    """,
    # Path description; tells user which directions are possible
    f"""
    To the North, is an overgrown path which weaves,
    seemingly endlessly, into the abyss of the woods.
    South leads back to the cottage.
    To the East, a path darker still than that which you have come.
    To your West, sunlight stream through the trees.
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("broken sword"),
    # List of searchable areas 
    ["brambles"],
    # Where the item can be found 
    "",
    # Links to other rooms
    {"north": "The Village Path", "south": "The Cottage",
        "east": "The Dark Woods", "west": "The Glade"},
    # Items required to enter this room 
    "cottage key"
)

# Creating a village_path Room
village_path = room.Room(
    # Room name
    "The Village Path",
    # Room decription
    """
    This winding path meanders back and forth,
    stitching itself through the trees. As you toil your way through
    you feel your legs ache. You can't say how long you've been walking.
    Finally, mercifully, you see before you a spire of a church.
    You pasue and take a breather. You notice a formation of leaves nearby.
    There also seems to be a faint shimmer by a nearby tree.
    """,
    # Path description; tells user which directions are possible
    """
    North of you is the church spire, jutting out above the canopy.
    South leads back to the woods.
    East, beyond a thick overgrowth, you hear the gentle trickle of water.
    West of you the path disappears, yet again, into a thick, black void.
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("rusted key"),
    # List of searchable areas 
    ["leaf pile", "nearby tree"],
    # Where the item can be found 
    "",
    # Links to other rooms
    {"north": "The Abandoned Church", "south": "The Woods",
        "east": "The River", "west": "The Dark Wood"},
    # Items required to enter this room 
    None
)

# Creating a church Room
chruch = room.Room(
    # Room name
    "The Abandoned Church",
    # Room decription
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
    # Path description; tells user which directions are possible
    f"""
    South leads back to the village path.
    East of the chuch the path continues,
    though little can be seen of a village.
    West of the church is a clearing of some sort.
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    [item.return_item("book"), item.return_item("torch")],
    # List of searchable areas 
    ["pulpit", "tabernacle", "table"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"south": "The Village Path", "east": "The Village", "west": "The Clearing"},
    # Items required to enter this room 
    None
)

# Creating a dark_woods Room
dark_woods = room.Room(
    # Room name    
    "The Dark Woods",
    # Room decription
    f"""
    Description of the dark woods
    """,
    # Path description; tells user which directions are possible
    f"""
    Description of the possible paths
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    [item.return_item("shortsword"), item.return_item("rope")],
    # List of searchable areas 
    ["black tree", "shiny object"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"south": "The Village Path", "east": "The Village", "west": "The Clearing"},
    # Items required to enter this room 
    "torch"
)

river = room.Room(
    # Room name    
    "The River",
    # Room decription
    f"""
    Description of the river
    """,
    # Path description; tells user which directions are possible
    f"""
    Description of the possible paths
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    [item.return_item("note"), item.return_item("arrows")],
    # List of searchable areas 
    ["black tree", "shiny object"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"south": "The Village Path"},
    # Items required to enter this room 
    "broken sword"
)

glade = room.Room(
    # Room name    
    "The Glade",
    # Room decription
    f"""
    Description of the glade
    """,
    # Path description; tells user which directions are possible
    f"""
    Description of the possible paths
    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    [item.return_item("golden key"), item.return_item("bow")],
    # List of searchable areas 
    ["black tree", "shiny object"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"south": "The Abandoned Church"},
    # Items required to enter this room 
    "broken sword"
)


# a set of all room objects
all_rooms = {
    cottage, woods, village_path, chruch, dark_woods, river, glade
}

def set_item_locations_for_each_room():
    for room in all_rooms:
        room.choose_random_item_location(room.searchable_areas)

def generate_room_from_name(name):
    """
    This function takes a string input and checks it against the names
    of the rooms. If the string matches a name, it returns the room object.
    """
    for room in all_rooms:
        if name == room.name:
            return room
