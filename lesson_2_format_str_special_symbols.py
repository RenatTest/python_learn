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