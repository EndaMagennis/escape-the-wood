# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def get_user_input():
    """
    Ask user to input their name and print a
    welcome message.
    """
    player_name = input("Enter your name:\n")
    print(f"Welcome, {player_name}. Your journey begins here.")


def main():
    get_user_input()


main()
