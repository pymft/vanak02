from random import randint


secret = randint(1, 1024)


while True:
    guess = int(input("guess the number"))

    if guess > secret:
        print("guess number is \033[32;1m greater\033[0m than secret number")
    elif guess < secret:
        print("guess number is \033[31;1m lesser \033[0m than secret number")
    else:
        print("BINGO")
        break











