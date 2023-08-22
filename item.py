FINDABLE_ITEMS = {
    # dictionary entries for types of items which can be found in the game
    "weapons": {
        "broken sword": 10,
        "shortsword": 30,
        "dagger": 25,
        "mace": 35,
        },
    "keys": {
        "cottage key": "key to the cottage",
        "golden key": "key with a golden hue",
        "rusted key": "an old key, brittle and rough"
    },
    "notes": {
        "note": "I've found it, finally",
    }
}


def return_item(request):
    """
    A function to return an item from the FINDABLE_ITEMS dictionary
    """
    for id, items in FINDABLE_ITEMS.items():
        for key, value in items.items():
            if request == key:
                return {key: value}
