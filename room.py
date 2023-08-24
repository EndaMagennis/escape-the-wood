import random
from time import sleep
import sys

class Room:
    """
    Creates an instance of the Room class.
    Rooms have inventories, item locations
    and paths to other rooms
    """
    def __init__(
                self, name, description, path_descriptions, event_description, inventory,
                searchable_areas, item_location, linked_rooms, required_item, 
                item_found, has_been_visited, has_event, has_encounter
                ):
        self.name = name
        self.description = description
        self.path_descriptions = path_descriptions
        self.event_description = event_description
        self.inventory = inventory
        self.searchable_areas = searchable_areas
        self.item_location = item_location
        self.linked_rooms = linked_rooms
        self.required_item = required_item
        self.item_found = item_found
        self.has_been_visited = has_been_visited
        self.has_event = has_event
        self.has_encounter = has_encounter

    def type_descritions(self, description):
        """
        Method gives a typed effect to the desription when 
        the user first visits the room.
        On subsequent visits, the desriction is simply printed.
        """
        if not self.has_been_visited:
            for char in description:
                sleep(0.02)
                sys.stdout.write(char)
                sys.stdout.flush()
        else:
            print(description)

    def describe_room(self):
        """
        Describes the instance of a room.
        """
        print(self.name)
        self.type_descritions(self.description)
        self.describe_event()

    def describe_paths(self):
        """
        Describes the North, South, East and West paths from current room
        """
        print(self.name)
        self.type_descritions(self.path_descriptions)

    def describe_event(self):
        if self.has_event:
            self.type_descritions(self.event_description)
        else:
            return

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
