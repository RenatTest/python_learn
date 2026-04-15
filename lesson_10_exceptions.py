# ---------- Lesson 10 exceptions ----------

# age = int("ten") #      ValueError

# num = 12 / 0 #          ZeroDivisionError

# if 22 > 12:
#  print("w") #           SyntaxError / IndentationError

# d = {
#     1: "first"
# }
# d[13] #                 KeyError

# d = [1,2,3]
# d[13] #                 IndexError

# КОД НИЖЧЕ НЕ ВИКОНУЄТЬСЯ !!!

# ---------- TRY - EXCEPT - ELSE (optional) - FINALLY (optional) ----------

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
            raise ValueError # make own error!
    except:
        print("Not an option, please choose 1 or 2")
        continue         
    else:
        print(f"player1: {player1}, player2: {player2}")
        break
