import item


class Room:

    def __init__(self, name, description, inventory, searchable_area):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.searchable_area = searchable_area

    def describe_room(self):
        
        print(self.description)


cottage = Room(
    "Cottage", """A small, rustic, thach rooved house.
    It's barren interior only hinting at a life which once resided within""",
    item.return_item("cottage key"), {}
    )
