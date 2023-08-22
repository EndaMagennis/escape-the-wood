import item


class Room:
    """
    Creates an instance of the Room class.
    """
    def __init__(self, name, description, inventory, searchable_areas, map_location):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.searchable_areas = searchable_areas
        self.map_location = map_location

    def describe_room(self):
        """
        Describes the instance of a room.
        """
        print(self.description)


# creating a 'cottage' room instance
cottage = Room(
    "The Cottage", f"""A small, rustic, thach rooved house.
    It's barren interior only hinting at a life which once resided within.
    In the western corner of the room you see a bookshelf.
    in the center of the room there is a large bed.
    Next to the bed, there is a cabinet
    """,
    item.return_item("cottage key"), ["bookshelf", "cabinet", "bed"], (0, 0)
    )
