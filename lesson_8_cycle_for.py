# ---------- Lesson 8 cycle for ----------

# for i in range(10): # range - generate numbers from 0 to 9
#     print(i)

# for i in range(1, 10): # from 1 to 9
#     print(i)

# for i in range(1, 10, 3): # 3 - step
#     print(i)

# name = "Renat"    
# for i in name:
#     print(i)

# list = [1, 3, 5, 6, 20]    
# for i in list:
#     print(i)

# users = ["Renat", "Vita", "Renata", "Rehina"]    
# for user in users:
#     print(user)

# numbers = [1, 2, -3, -5, 388] # filter elements
# for number in numbers:
#     if number >= 0:
#         print(number)

# EXAMPLE

player1 = "X"
player2 = "0"

BOARD = [["X", "0", "0"],
         ["X", "X", "0"],
         ["0", "X", "X"]]

for player in [player1, player2]:
    # check main diagonal
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == player:
        print(f"Player {player} won")
    # check side diagonal    
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] == player:
        print(f"Player {player} won")    

for i in range(len(BOARD)):
    # check rows
    if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == player1:
        print(f"Player {player1} won")
        break
    elif BOARD[i][0] == BOARD[i][1] == BOARD[i][2] == player2:
        print(f"Player {player2} won")
        break
    # check columns    
    elif BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == player1:
        print(f"Player {player1} won")
        break
    elif BOARD[0][i] == BOARD[1][i] == BOARD[2][i] == player2:
        print(f"Player {player2} won")
        break

# Practice 

POSITIONS =  {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}    

# Practice 2

player = "X"

BOARD2 = [["O", "O", "X"],
        ["O", "X", "O"],
        ["X", "X", "X"]]

for row in range(3):
    if BOARD2[row][0] == BOARD2[row][1] == BOARD2[row][2] == player:
        print(f'Match in row {row}')