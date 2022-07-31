print("\033[1;31m--------------\033[0;0m\033[1;33mCASINO\033[0;0m\033[1;31m---------------\033[0;0m")
print("Hello! You are in a virtual casino!")
print("You have 5 attempts to guess the number and color.")
print("Numbers from \033[1;36m1 to 10\033[0;0m and the color is \033[1;31mred\033[0;0m or \033[1;37mwhite\033[0;0m")
print("If you are ready to start, then write \033[1;32m'GO'\033[0;0m")
exi = input("If you want to leave write \033[1;31m'EXIT'\033[0;0m:")
if exi == "GO" or exi == "go" or exi == "Go" or exi == "gO" or exi == " go":
    print("\033[1;31m---------\033[0;0m\033[1;33mTHE GAME STARTED\033[0;0m\033[1;31m----------\033[0;0m")
    a = []
    while True:
        import random
        from random import randint
        num_ps = int(input("Enter the number: "))
        color_ps = (input("Enter the color: "))
        color_mas = ['red', 'white']
        color = random.choice(color_mas)
        num = randint(1, 10)
        if num_ps == num:
            print(f"\033[1;32m >>> You guessed! Number \033[0;0m |{num}|")
        else:
            print(f"\033[1;31m >>> You didn't guess! There was a number: \033[0;0m |{num}|")
        if color_ps == color:
            if color == "red":
                print("\033[1;32m >>> You guessed the color! \033[0;0m" + "\033[1;34;41m RED \033[0;0m")
            else:
                print("\033[1;32m >>> You guessed the color! \033[0;0m" + "\033[1;34;47m WHITE \033[0;0m")
        else:
            print(f"\033[1;31m >>> You didn't guess the color! Сolor was: \033[0;0m |{color}|")

        a.append(1)
        if len(a) > 4:
            print(">>> You missed your chance!")
            print("--------------------")
            print("\033[1;31m !!! GAME OVER !!! \033[0;0m")
            print("--------------------")
            break

        if num_ps == num and color_ps == color:
            print("\033[1;31m ---------------------- \033[0;0m")
            print("\033[1;35mHURRAH!\033[0;0m \033[1;34mYOU\033[0;0m \033[1;33mWON\033[0;0m \033[1;36mA\033[0;0m \033[1;31mCAR!\033[0;0m")
            print("\033[1;31m ---------------------- \033[0;0m")
            break
elif exi == "Exit" or exi == "exit" or exi == "EXIT" or exi == " exit":
    print("\033[1;31m-----------------------------------\033[0;0m")
    print("You are missing out on your happiness!")
else:
    print("I don't understand you!")