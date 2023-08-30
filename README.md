# Escape The Woods

![Banner Image](documentation/documentation-banner-image.png)

Link to [Deployed App](https://escape-the-wood-d0f5272a8865.herokuapp.com/)

## Background to Escape the Woods
Escape the Woods is a [Python](https://www.python.org/) terminal application which is an homage to old-school, text-based adventure games.
Text-based adventure games like [Zork](https://en.wikipedia.org/wiki/Zork) were among the first interactive media accessible on computers. Given that they only require user input, they lend themselves perfectly to input validation.

## How to Play

1. Click [here](https://escape-the-wood-d0f5272a8865.herokuapp.com/) to access the app
2. The app will begin automatically.
3. Read the introduction carefully 
4. Input your name
5. Read the description and input at least 3 letters of your chosen action
6. Visit areas, collect items, read descriptions and survive
7. Know that some areas require items to progress
8. To 'win' you must visit all rooms and defeat both enemies
9. Encounters with enemies require specific items(weapons)
10. Engaging in an encounter without a weapon will end in defeat
11. Restart the game
12. Become frustrated, like the good old days

You can find a guide below on exact steps to take to win

---
## User Stories
### First-time Users
 - As a first-time user, I want to understand how to interact with the app
 - As a first-time user, I want clear objectives
 - As a firt-time user, I want the app to anticipate my inputs and work regardless of what I type

 ### Returning Users
 - As a returning user, I want to be able to finish the game in an efficient way
 - As a returning user, I want to be able to take different routes

---

 ## Features
 
- ASCII logo during the intro

[Ascii Art](https://en.wikipedia.org/wiki/ASCII_art) uses strings of characters and special characters to create images and can be printed to consoles relatively easily.

![Ascii logo](documentation/documentation-ascii-logo.png)

- Introduction

The introduction gives the user the goal of the game and incentivises paying careful attention to the descriptions of places and items. It also forewarns the player that they should be wary of encounters if they do not have the correct gear.

![Introduction](documentation/documentation-introduction.png)

- Prompt to enter a name and first room description

As seen above, after the introduction, the user is then prompted to enter a name, the input is validated and a welcome message is printed. The user is then itroduced to the world, in the first room.

![Welcome and first room](documentation/documentation-welcome-message.png)

- Colors

Using the [colorama library](https://pypi.org/project/colorama/), color is added to certain texts. This is to create a better user experience and highlight key actions the user can take

![Colors](documentation/documentation-colors.png)

- Action functions

Throuout the game, the user is promted to input an action verb to trigger an action; "search", "move", "look", "use", "describe", "end game", and "help" all correspond to an in-game method. How the inputs are checked allows users to input only a partial string, e.g., "he" to run the help method.

![Help method](documentation/documentation-help.png)

---
## Flowcharts

The logic of the game is a loop. While the player is "alive" they are continually prompted to input actions until certain game conditions are met.

- Initial chart with no encouter system

![Initial flowchart](documentation/documentation-first-flowchart.png)

- Flowchart with encounter system

![Flowchart with encounters](documentation/documentation-encounter-flowchart.png)

---

## Technologies

### Languages

- [Python 3.11.3](https://www.python.org/downloads/release/python-3113/): Used as the foundation for logic of the app (80.2%)

- [HTML](https://www.w3schools.com/html/html_intro.asp): Part of the CI Template, used to format the host webpage

- [Javascript](https://www.w3schools.com/js/): Also part of the CI template, used for webpage logic

### Libraries and Tools
#### Native Python Library Imports

- [random](https://docs.python.org/3/library/random.html): used to randomise item locations in rooms

- [time](https://docs.python.org/3/library/time.html): used to import the [sleep](https://docs.python.org/3/library/time.html#time.sleep) method to wait x number of seconds at certain points

- [sys](https://docs.python.org/3/library/sys.html): used to create a typing effect using the [sys.stdout](https://docs.python.org/3/library/sys.html#sys.stdout).write() method in conjunction with the sleep method above, and the sys.stdout.flush() method to clear the stdout buffer.

- [os](https://docs.python.org/3/library/os.html): used [os.system](https://docs.python.org/3/library/os.html#os.system) to prevent user input during typing effect, and used [os.name](https://docs.python.org/3/library/os.html#os.name) to clear the terminal regardless of current operating system.

#### Third Party Imports

- [colorama](https://pypi.org/project/colorama/): used to import Fore to change the color of terminal output.

#### Other Tools:

- [VSCode](https://code.visualstudio.com/) IDE and code editor used to write code
- [Git](https://git-scm.com/) was used for version control
- [GitHub](https://github.com/) was used to store the code to a cloud repository
- [GIMP](https://www.gimp.org/) was used to trim and alter PNGs used in documentation
- [Heroku](https://signup.heroku.com/) was used to deploy the terminal app online

--- 

## Bugs and Fixes

+ Input Validation:
    - Player could input special characters
        - Fix: 
        ```python
        for char in input:
                ...
                elif not char.isalnum():
                    raise TypeError
            return True
        ```
    - Player could leave blank input
        - Fix:
        ```python
        elif not bool(input):
            raise ValueError
        ```
    - Player could not use spaces
        - Fix:
        ```python
        else:
            for char in input:
                if char.isspace() and not input.isspace():
                    continue
        ```
    - Name containing spaces would not capitalize after space
        - Fix:
        ```python
        else:
        ...
        print(f"Hello, {player_name.title()}. Your journey begins in:\n")
        ```


