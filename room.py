import random

class Room:
    """
    Creates an instance of the Room class.
    Rooms have inventories, item locations
    and paths to other rooms
    """
    def __init__(
                self, name, description, path_descriptions, inventory,
                searchable_areas, item_location, linked_rooms, required_item, item_found
                ):
        self.name = name
        self.description = description
        self.path_descriptions = path_descriptions
        self.inventory = inventory
        self.searchable_areas = searchable_areas
        self.item_location = item_location
        self.linked_rooms = linked_rooms
        self.required_item = required_item
        self.item_found = item_found

    def describe_room(self):
        """
        Describes the instance of a room.
        """
        print(self.name)
        print(self.description)

    def describe_paths(self):
        """
        Describes the North, South, East and West paths from current room
        """
        print(self.name)
        print(self.path_descriptions)

    def choose_random_item_location(self, searchable_areas):
        """
        Randomly selects which of the searchable areas holds the item
        """
        searchable_areas = self.searchable_areas
        # choosing a random area to place the item
        random_choice = random.randint(0, len(searchable_areas) - 1)
        selected_area = searchable_areas[random_choice]

        # setting the room's item_location to the selected_area
        self.item_location = selected_area
        return selected_area
