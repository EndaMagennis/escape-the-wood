FINDABLE_ITEMS = {
    # dictionary entries for types of items which can be found in the game
    "weapons": {
        "broken sword": "Useless as a weapon, but the edge could hack a few branches!",
        "shortsword": "Well balanced and swift, this blade will serve you well!",
        "mace": "A brutal weapon, but great for taking care of wild beasts",
        "bow": "Great for enemies at a distance!",
    },
    "keys": {
        "cottage key": "key to the cottage",
        "rusted key": "an old key, brittle and rough"
    },
    "notes": {
        "book": "A Teological examination of the Old Gods",
    },
    "equipment": {
        "torch": "Already oiled, and with a striker to boot!",
        "arrows": "A bundle of 10 arrows"
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

def return_item_description(request):
    
    """A funtion to return an item descrition"""
    for out_key, out_value in FINDABLE_ITEMS.items():
        for in_key, in_value in out_value.items():
            if request == in_key:
                return in_value
            
