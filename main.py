# ---------- Lesson 1 Variables ----------

message = "Lets play" # змінна типу str
age = 39 # змінна типу int
pi = 3.14 # змінна типу float
signs = ["X", "O", "O", "X",] # змінна типу list
players = {1: "X", 2: "O"} # змінна типу dict;  players[1] - get value

# Створити змінну на основі іншої
# message2 = message
# id(message) = id(message2) - це одна і та ж сама комірка в пам'яті

# Називати змінні
# snake_case
# змінна іменник

# ---------- Lesson 2 Format str, special symbols ----------

message2 = "Player X won!"
message3 = 'Player X won!'

# multi line string

message4 = """ 
Player X won!
Congrats!
"""

message5 = "Player X won!\nCongrats!"

# dynamic string, formatted string

winner = "Renata"
loser = "Pasha"
message6 = f"Player {winner} won! Congrats!\nPlayer {loser} lost! Foo!"  

# Const

# MENU = 'Hello! Welcome to Tic Tac Toe game!\nRules: X and O takes turns marking the spaces in a 3*3 grid'

MENU = """
Hello! Welcome to tic tac toe game!
Rules: X and O takes turns on the grid 3x3
"""

# print(MENU)

player = 'X'
PLAYER_WON_MESSAGE = f'Player {player}, you won!'
# print(PLAYER_WON_MESSAGE)

# ---------- Lesson 3 input() ----------

# control + C - end of program
# winner = input('Winner enter your sign >>> ') 
# loser = input('Loser enter your sign >>> ') 

message = f"Player {winner} won! Congrats! Player {loser} lost! Foo!"  

# print(message)
# print(type(winner)) # str always

# sign = input('Please enter your sign:')
# print(f'Player {sign}, your turn!')

# ---------- Lesson 4 casting types ----------

SIGNS = {
    1: "X",
    2: "0",
}

# convert str to int - function int()
# Додавання рядків - конкатенація
# Множення рядків - "22" * 2 = '2222'

winner_sign = int(input('Please choose a sign [1: X, 2: O] >>> ')) 
print(winner_sign)
print(type(winner_sign))
message_winner = f'Player {SIGNS[winner_sign]} is winner'
print(message_winner)

# convert int to str - function str()
int_from_str = str(88)
print(int_from_str)
print(type(int_from_str))

# convert str to float - float()
str_to_float = float("88.88")
print(str_to_float)
print(type(str_to_float))

# True and False
age = 20
is_adult = age > 18
is_child = age < 18
print(is_adult)
print(is_child)
# 0 - False, number not 0 - True
# bool("str") - True
# bool("") - False

# None
name = None
print(name)

# Залишок від ділення %
turn_number = 5
print(turn_number % 2 == 0) # False
print(turn_number % 2 == 1) # True

# Prctice
choice = int(input("Player 1, what's your sign [choose 1:X or 2:O]: "))
print(choice % 2 == 0)
