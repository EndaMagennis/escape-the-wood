FINDABLE_ITEMS = {
    # dictionary entries for types of items which can be found in the game
    "weapons": {
        "broken sword": f"""
Useless as a weapon, but the edge could hack a few branches!
        """,
        "shortsword": f"""
Well balanced, sharp, and swift, this blade will serve you well!
        """,
        "mace": f"""
A brutal weapon, but great for taking care of wild beasts
        """,
        "bow": f"""
Great for enemies at a distance!
        """,
    },
    "keys": {
        "cottage key": f"""
Key to the cottage
        """,
        "rusted key": f"""
An old key, brittle and rough
        """
    },
    "notes": {
        "book": f"""
    Theobald Bantreck's Rules for Survival:

Always be prepared to meet a goblin by flowing water
They have been known to ransack unsuspecting people by rivers.
A sharp blade is usually more than enough to deal with them.
        """,
    },
    "equipment": {
        "torch": f"""
Already oiled, and with a striker to boot!""",
        "arrows": f"""
A bundle of 10 arrows"""
    }
}


def return_item(request):
    """A function to return an item from the FINDABLE_ITEMS dictionary"""

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
