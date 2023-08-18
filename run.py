# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

intro = """\nYou have awoken in a ramshackel abode on the outskirts of a town.
You have no recollection of who you are or how you've gotten here.
A voice calls out to you, seemingly from nowhere.\n
'Ho, there weary traveller, you are here for the Challenge of Kings.
That you have awoken is a testament in itself.
Now piece yourself together. Who are you?'\n
Your head begins swimming; the past rushing to meet the present.
You suddenely remember yourself.\n"""


def get_user_input():
    """
    Ask user to input their name and print a
    welcome message.
    """

    try:
        player_name = (input("Enter your name: "))
        if not player_name.isalpha():
            raise TypeError
        elif len(player_name) < 3:
            raise ValueError
        print(f"Welcome, {player_name}. Your journey begins here.")

    except TypeError:
        print("""How could ones name consist of anything but letters?
Surely you lie!\n""")
        get_user_input()

    except ValueError:
        print("""Drawing a blank are we? Come now, what is your full name?
Only titles have fewer than 3 letters\n""")
        get_user_input()


def main():
    print(intro)
    get_user_input()


main()
