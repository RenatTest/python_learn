# ---------- Lesson 5 if / else ----------

age = int(input("What's your age?"))

print("Welcome to the bar!")

if age > 18:
    print("Here is your beer!")
elif age == 18:
    print("Congrats, your first ever beer and i hope the last one!")    
else:
    print("You are too young!")

# debug with breakpoints

# if / else with 2 vars

age2 = int(input("Age >>> "))
gender = input("Genfer >>> ")

if age2 < 18:
    if gender == "M":
        print("son")
    else:
        print("daughter")
elif age2>= 18 and age2 < 65:
    if gender == "M":
        print("father")
    else:
        print("mother")
else:
    if gender == "M":
        print("grandfather")
    else:
        print("grandmother")

name = "Renat"

if name:
    print("Hello") # Not emppty str always True

# GAME

INTRO_MESSAGE = """
    Hello! Welcome to Tic Tac Toe game!

    Rules: Player 1 and player 2, represented by X and 0, take turns 
    marking the spaces in a 3x3 grid. The player who succeeds in placing
    three of their marks in horizontal, vertical or diagonal row wins.
"""

choice3 = int(input("Player 1, what's your sign? [choose 1: X or 2: 0] >>> "))
if choice3 == 1:
    player1 = "X"
    player2 = "0"
    print('Player1 - X, Player2 - 0')
elif choice3 == "2":
    player1 = "0"
    player2 = "X"
    print('Player1 - ), Player2 - X')
else:
    print("Not an option, please choose 1 or 2")


# Practice

has_winner = bool(input("Is there a winner: "))
count = int(input("What turn is it: "))

if has_winner or count == 9:
    print('Game is over!')
else:
    print('Keep playing!')

# Practice 2

choice = int(input("Player 1, what's your sign? [choose 1:X or 2:O]: "))
    
if choice == 1:
    player1 = "X"
    player2 = "O"
elif choice == 2:
    player1 = "O"
    player2 = "X"
else:
    print('Not an option')    