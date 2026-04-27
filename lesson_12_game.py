# ---------- Lesson 12 game ----------

INTRO_MESSAGE = """
    Hello! Welcome to Tic Tac Toe game!

    Rules: Player 1 and player 2, represented by X and 0, take turns 
    marking the spaces in a 3x3 grid. The player who succeeds in placing
    three of their marks in horizontal, vertical or diagonal row wins.
"""

BOARD = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

POSITIONS = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

def display_board_coordinates():
    pattern = """
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """
    print(pattern)

# check for winner
def check_board_state(player1, player2):
    winner = False
    for i in range(3):
        # check rows
        if (BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == player1):
            winner = True
            print(f"Player {player1}, you won, on row!")
        elif (BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == player2):
            winner = True
            print(f"Player {player2}, you won, on row!")
        # check columns
        elif (BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == player1):
            winner = True
            print(f"Player {player1}, you won on column!")
        elif (BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == player2):
            winner = True
            print(f"Player {player2}, you won on column!")

    # check diagonals
    for player in [player1, player2]:
        if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == player:
            winner = True
            print(f"Player {player}, you won on main diagonal!")
        elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == player:
            winner = True
            print(f"Player {player}, you won on side diagonal!")

    return winner            

def display_board():
    print("\n")
    for row in range(3):
        print(f" {BOARD[row][0]} | {BOARD[row][1]} | {BOARD[row][2]} ")
        if row != 2:
            print("---+---+---")
    print("\n")\

def make_choice(player1, player2, count):
    current_player = player1
    if count % 2 == 0:
        current_player = player2
    print(f"Player {current_player}, it is your turn. ")
    while True:
        try:
            choice = input("Use [p] for positions, [1-9] for cells ")
            choice = choice.lower()
            if choice == "p":
                display_board_coordinates()
                continue

            choice = int(choice)
            if choice < 0 or choice > 9:
                raise ValueError
            
            row, column = POSITIONS.pop(choice)
        except ValueError:
            print("Not an option. Use [p] for positions, [1-9] for cells")
        except KeyError:
            print("Cell is already filled")
        else: 
            break

    BOARD[row][column] = current_player      

# 1. Show intro message 
print(INTRO_MESSAGE)

# 2. Show playboard
print("Here is the playboard")
display_board_coordinates()

# 3. Choose sign
while True:
    try:
        choice = int(input("Player 1, what's your sign [choose 1 or 2]: \n1: X \n2: 0\n>>>"))
        if choice == 1:
            player1 = "X"
            player2 = "0"
        elif choice == 2:
            player1 = "0"
            player2 = "X"
        else:
            raise ValueError
    except:
        print("Not an option, please choose 1 or 2")
        continue
    else:
        print(f"Player1: you are {player1}")
        print(f"Player2: you are {player2}")
        break  

# 4. Play while we have no winner

has_winner = False
count = 1
while has_winner == False and count < 10:
    make_choice(player1, player2, count)
    display_board()

    has_winner = check_board_state(player1, player2)
    count += 1

    if count == 9:
        print("Tne board is full. Game over.")
        if not has_winner:
            print("There is a tie.")



