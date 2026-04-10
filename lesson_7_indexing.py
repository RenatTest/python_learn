# ---------- Lesson 7 indexing ----------

# python3 -> l = [1,2,3] -> l. + tab + tab -> methods of the list

# l.append(-5) -> add new element in the end of list
# l.sort(reverse=True) -> sort elements reversed
# l.remove(2) -> remove element
# l[2] -> get element by index
# l[-1] -> get element by index reversed
# len(l) -> get length of list

# str = 'Armstrong'

# str[2] -> get element by index
# str[-1] -> get element by index reversed
# len(str) -> get length of string

# l = ["banana","apple","mango"]
# l.append(12) - you can add element of different type (bool, list ...)

# CREATE BOARD
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# board[0][0] -> 1
# board[1][1] -> 5
# board[1][1] = 'X'
# board[0][2] = '0'

# l[1:4] -> get 1,2,3 element
# fruits = l[:3] -> create new list from 0 to 2 elements of list l
# fruits = l[3:] -> create new list from 3 to end of list l

# EXAMPLE

player1 = "X"

BOARD = [["X", " ", " "],
         [" ", "X", " "],
         [" ", " ", "X"]]

if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == player1:
    print(f"Player {player1} won")
else: 
    print(f"Player {player1} not won")

# Practice

BOARD = [["", "", ""],["", "", ""],["", "", ""]]

BOARD = [["X", " ", " "],
        [" ", "X", " "],
        [" ", " ", "X"]]

player1 = "X"


if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == player1:
   print('Player 1 won!')

