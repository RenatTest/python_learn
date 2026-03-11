# ---------- Lesson 6 string methods ----------

text = "to be or not to be"

text.find("be") # search some text - return element where begin word (3)
text.upper() # make all word uppercase
text.split() # return the list of strings
text.rstrip("be") # delete last word (be)
text.capitalize() # return copy of text with first big letter
text.isdigit() # return True or False (check numbers, 1 not a number - False)
text.isalpha() # return True or False (check string, 1 not a string - False)

# terminal - text. + 2 tabs - see all methods
# help(print) - info about method
# q - exit

pattern = """
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
"""

choice = input("Player 1, what's your sign? [choose 1: X or 2: 0, [b] for board] >>> ")

if choice.isdigit():
    choice = int(choice)
    if choice == 1:
        player1 = "X"
        player2 = "0"
    elif choice == 2:
        player1 = "0"
        player2 = "X"
    else:
        print("Not an option, please choose 1 or 2")
        player1 = None
        player2 = None
    print(f'Player1 - {player1}, Player2 - {player2}')    
else:
    if choice.lower() == "b":
        print(pattern)
    else:     
        print("You entered a letter not a number or [b]")

# Practice 1
BOARD = [["O", "O", "X"],
        ["O", "X", "O"],
        ["X", "X", "X"]]

choice2 = input('Choose [b] to print the board: ')
if choice2.lower() == "b":
    print(BOARD)
else:
    print("Not an option")        

# Practice 2
choice3 = input('Choose [1-9] to pick the cell: ')
if choice3.isdigit():
    print(f"Cell {choice3} selected")
else:
    print("Not an option")
