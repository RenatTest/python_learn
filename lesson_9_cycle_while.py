# ---------- Lesson 9 cycle while ----------

i = 0

while i < 10:
    print(i)
    i += 1

# while True:
#     print('Hello') - endless cycle

# Example

number = 555

quess = int(input("Guess my number between 1 and 1000: "))

while quess != number:
    if quess > number:
        print(quess, "is too high")
    elif quess < number:
        print(quess, "is too low")
    quess = int(input("Guess again: "))
        
# Example game

while True: 
    choice = input("Player 1, what's your sign [choose 1 or 2]: \n1: X \n2: 0\n>>>")
    if not choice.isdigit():
        print("Not an option, please choose 1 or 2")
        continue
    choice = int(choice)
    if choice == 1:
        player1 = "X"
        player2 = "0"
        print(f"player1: {player1}, player2: {player2}")
        break 
    elif choice == 2:
        player1 = "0"
        player2 = "X"
        print(f"player1: {player1}, player2: {player2}")
        break 
    else:
        print("Not an option, please choose 1 or 2")
           