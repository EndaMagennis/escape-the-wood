FINDABLE_ITEMS = {
    # dictionary entries for types of items which can be found in the game
    "weapons": {
        "broken sword": 10,
        "shortsword": 30,
        "dagger": 25,
        "mace": 35,
        "bow": 35,
    },
    "keys": {
        "cottage key": "key to the cottage",
        "golden key": "key with a golden hue",
        "rusted key": "an old key, brittle and rough"
    },
    "notes": {
        "note": "I've found it, finally",
        "book": "A Teological examination of the Old Gods",
    },
    "equipment": {
        "torch": 10,
        "rope": "50 feet",
        "arrows": 10
    }
}


def return_item(request):
    """
    A function to return an item from the FINDABLE_ITEMS dictionary
    """
    for out_key, out_value in FINDABLE_ITEMS.items():
        for in_key, in_value in out_value.items():
            if request == in_key:
                return in_key



