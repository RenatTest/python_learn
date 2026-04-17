# ---------- Lesson 11 functions ----------

# simple function

def print_first_n_positive_numbers():
    n = int(input(">>> "))
    for i in range(n):
        print(i)

print_first_n_positive_numbers()

# function with parameters

# parameters in fumction
def print_first_n_positive_numbers(start, n = 5): # n = 5 - parameter by default
    for i in range(start, n):
        print(i)

# arguments in call
print_first_n_positive_numbers(-5, 10) 
print_first_n_positive_numbers(start = -5, n = 10) # simple syntax

# EXAMPLE

BOARD = [["X", "0", "0"],
         ["X", "X", "0"],
         ["0", "X", "X"]]

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

# POSITIONS.pop() # delete first key

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
def check_board_state():
    pass # pass - заглушка

def display_board():
    print("\n")
    for row in range(3):
        print(f" {BOARD[row][0]} | {BOARD[row][1]} | {BOARD[row][2]} ")
        if row != 2:
            print("---+---+---")
    print("\n")\
    
display_board()

def make_choice(player1, player2, count):
    pass

# Practice

BOARD = [["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "X", "X"]]

player = "X"

def check_diagonal(player):
     # check main diagonal
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == player:
        return True
    # check side diagonal    
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == player:
        return True
    else:
        return False
    
player_won = check_diagonal(player)

print(player_won)

# Practice 2

BOARD = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]

row = int(input("row: "))
column = int(input("column: "))
player = input("player's sign: ")

def update_board(row, column, player):
        BOARD[row][column] = player

update_board(row, column, player)

print(BOARD)