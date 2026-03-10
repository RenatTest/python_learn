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

# Practice
choice = int(input("Player 1, what's your sign [choose 1:X or 2:O]: "))
print(choice % 2 == 0)