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

MENU = """

Hello! Welcome to tic tac toe game!
Rules: X and O takes turns on the grid 3x3

"""

print(MENU)
