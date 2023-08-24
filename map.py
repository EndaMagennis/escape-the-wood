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
    A small, rustic, thatch roofed house.
    It's barren interior only hinting at a life which once resided within.
    In the western corner of the room you see a bookshelf.
    In the center of the room there is a large bed.
    Next to the bed, there is a cabinet.

    """,
    # Path description; tells user which directions are possible
    """
    Outside, north of you, appears to be a woodland.
    However, the door appears to be locked.

    """,
    None,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("cottage key"),
    # List of searchable areas 
    ["bookshelf", "cabinet", "bed"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"north": "The Woods"},
    # Items required to enter this room 
    "",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting the event boolean
    False,
    # Setting has_encounter
    False
)

# Creating a cottage Room
woods = room.Room(
    # Room name
    "The Woods",
    # Room decription
    f"""
    A dark and damp wood engulfs the path before you.
    Barely a speck of sunlight can be seen.
    Your eyes struggle to focus. Your legs carry you forward, like
    some sort of wretched automoton. Soon, you come to a fork in the woods.
    A thick net of brambles seems to conceal a glimmer.

    """,
    # Path description; tells user which directions are possible
    f"""
    To the North is an overgrown, but visible, trail.
    South leads back to the cottage.
    To the East, the trees blacken as the light itself is swallowed.
    To your West, sunlight streams through the trees, 
    though overgrowth blocks your way.

    """,
    None,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("broken sword"),
    # List of searchable areas 
    ["brambles"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"north": "The Village Path", "south": "The Cottage",
        "east": "The Dark Woods", "west": "The Glade"},
    # Items required to enter this room 
    "cottage key",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    False,
    # Setting has_encounter
    False
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
    You pasue and take a breather. You notice a deliberate formation of leaves.
    There also seems to be a faint shimmer by a nearby tree.

    """,
    # Path description; tells user which directions are possible
    """
    North of you is the church spire, jutting out above the canopy.
    South leads back to the woods.
    East, the path contiues, more certain, and prominent.
    West of you, the sound of water can be faintly heard.

    """,
    # Event description
    None,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("rusted key"),
    # List of searchable areas 
    ["leaf pile", "nearby tree"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"north": "The Abandoned Church", "south": "The Woods",
        "east": "The Village", "west": "The River"},
    # Items required to enter this room 
    "cottage key",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    False,
    # Setting has_encounter
    False
)

# Creating a river Room
river = room.Room(
    # Room name    
    "The River",
    # Room decription
    f"""
    The tranquil trum of the water against the rock
    brings peace to your mind. You feel the crushing weight 
    of your situation lift from your chest. 

    """,
    # Path description; tells user which directions are possible
    f"""
    East leads back to the village path.
    North, the path winds beyond your vision.

    """,
    # Event description
    f"""
    Nearby you see a shape up-river. It begins gaining momentum.
    Before long the shape is upon you, a goblin, armed with a mace.
    He swings the mace, barely missing you. It's a fight.
    How will you respond?

    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("mace"),
    # List of searchable areas 
    ["goblin corpse"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"north": "The Abandoned Church", "east": "The Village Path"},
    # Items required to enter this room 
    "shortsword",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    True,
    # Setting has_encounter
    True
)

# Creating a village Room
village = room.Room(
    # Room name    
    "The Village",
    # Room decription
    f"""
    Decay and time have had their way with this place.
    The wood frames have become blackened with mold.
    Mycelium and fungus intricately weave through every inch of
    walls, the doors of each bungalow ling since turned to mush.
    
    """,
    # Path description; tells user which directions are possible
    f"""
    West leads back to the village path.
    South, the darkness of thick forestry envelops your vision.
    North you can see the spire eeking above the trees.

    """,
    # Event description
    """
    As you amble back and forth trough the houses, you spot a rusted
    metal chest; inoculated against the worst of the decay. 

    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("shortsword"),
    # List of searchable areas 
    ["rusted chest"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"north": "The Abandoned Church", "south": "The Dark Woods", "west": "The Village Path"},
    # Items required to enter this room 
    "rusted key",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    True,
    # Setting has_encounter
    False
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
    East of the chuch the path is more prominently.
    West of the church is a clearing of some sort.

    """,
    # Event description
    None,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("torch"),
    # List of searchable areas 
    ["pulpit", "tabernacle", "table"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"south": "The Village Path", "east": "The Village", "west": "The River"},
    # Items required to enter this room 
    "cottage key",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    False,
    # Setting has_encounter
    False
)

# Creating a dark_woods Room
dark_woods = room.Room(
    # Room name    
    "The Dark Woods",
    # Room decription
    f"""
    Even with the light of the torch, the darkness pervades.
    Shadows and imagined beasts dance in your periferies,
    shaking you to your core with each movement.
    Wind twists through the trees creating a cacophony of hollow tones.
    The macabre sounds dig into your psyche. You could swear that there 
    are voices calling out to you in anguish. Efforts to steel yourself
    are undone by the dark woodwind orchestra baying at you.

    """,
    # Path description; tells user which directions are possible
    f"""
    North seems to be nothing but more darkness.
    South of you, you could swear you saw a flicker of light.
    East is a beaten path that twists back and forth.
    West is the direction you came from.

    """,
    # Event description
    f"""
    After some time, your eyes adjust. The phantoms are no longer 
    antagonising you. Now, your worries are realised as a wolf bounds
    towards you. You must act fast. What will you do?

    """,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("arrows"),
    # List of searchable areas 
    ["black tree", "shiny object"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"south": "The Clearing", "east": "The Village", "west": "The Woods"},
    # Items required to enter this room 
    "torch",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    False,
    # Setting has_encounter
    True
)

# Creating a glade Room
glade = room.Room(
    # Room name    
    "The Glade",
    # Room decription
    f"""
    A small lake is encircled by vibrantly colored trees.
    The lake itself is teeming with life which, when approached,
    falls silent. Each cluster of trees is a gradient from lush green
    to a soft amber. Hues of brown and purple dotted throughout.

    """,
    # Path description; tells user which directions are possible
    f"""
    East leads back towords the woods.
    Thick forestry envelops all other directions.

    """,
    None,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("rusted key"),
    # List of searchable areas 
    ["green trees", "orange trees", "red trees", "lake"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"east": "The Woods"},
    # Items required to enter this room 
    "broken sword",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    False,
    # Setting has_encounter
    False
)

# Creating a clearing Room
clearing = room.Room(
    # Room name    
    "The Clearing",
    # Room decription
    f"""
    The wood seems to suddenly break apart here.
    Sunlight floods down upon you. You feel invigerated.
    The maddening darkness of the dark woods slides off you.
    You breath deeply. A small circle of stones hints at an old
    campsite fire. Logs encircle the fire; makeshift seats.
    There's an old lean-to just on the edge of the woods.

    """,
    # Path description; tells user which directions are possible
    f"""
    North is the direction you came from.
    All other directions look no different.

    """,
    # Event description
    None,
    # Calls the return_item function from the item script and adds it to the room inventory
    item.return_item("bow"),
    # List of searchable areas 
    ["lean-to"],
    # Where the item can be found 
    None,
    # Links to other rooms
    {"north": "The Dark Woods"},
    # Items required to enter this room 
    "cottage key",
    # Defaulting to false for item found 
    False,
    # Defaulting to false for has_been_visited
    False,
    # Setting has_event boolean
    False,
    # Setting has_encounter
    False
) 

# a set of all room objects
all_rooms = {
    cottage, woods, village_path, river, village,
    chruch, dark_woods, glade, clearing
}

def set_item_locations_for_each_room():
    """
    Function iterates through each room and runs 
    the choose_random_item_location method for each room 
    """
    for room in all_rooms:
        for item in room.inventory:
            item_location = room.choose_random_item_location(room.searchable_areas)
            room.item_location = item_location
    
    return item_location


def generate_room_from_name(name):
    """
    This function takes a string input and checks it against the names
    of the rooms. If the string matches a name, it returns the room object.
    """
    for room in all_rooms:
        if name == room.name:
            return room
