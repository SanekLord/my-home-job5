a = []
while True:
    import random
    from random import randint
    num_ps = int(input("Enter the number: "))
    color_ps = (input("Enter the color: "))
    color_mas = ['red', 'white']
    color = random.choice(color_mas)
    num = randint(1, 1)
    if num_ps == num:
        print(f">>> You guessed! Number |{num}|")
    else:
        print(f">>> You didn't guess! There was a number: |{num}|")
    if color_ps == color:
        print(f">>> You guessed the color! |{color}|")
    else:
        print(f">>> You didn't guess the color! Сolor was: |{color}|")

    a.append(1)
    if len(a) > 4:
        print(">>> You missed your chance!")
        print("-----------------")
        print("!!! GAME OVER !!!")
        print("-----------------")
        break

    if num_ps == num and color_ps == color:
        print("----------------------")
        print("HURRAH! YOU WON A CAR!")
        print("----------------------")
        break
