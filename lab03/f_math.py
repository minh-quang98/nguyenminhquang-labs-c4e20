from random import randint, choice
from eval import calc
# import eval
play = True
while play:
    x = randint(1,10)
    y = randint(1,10)
    er = choice([-1, 0, 1])
    op = choice(['+', '-', '*', '/'])
    res = calc(x, y, op)
    print(x, op, y,'=', res + er)
    ans = input("(Y/N)? ").upper()
    if res == res + er:
        if ans == "Y":
            print("Yay")
            print()
            print("Next:")
        else:
            print("Wrong")
            print("You lose")
            play = False
    else:
        if ans == "N":
            print("Yay")
            print()
            print("Next:")
        else:
            print("Wrong")
            print("You lose")
            play = False