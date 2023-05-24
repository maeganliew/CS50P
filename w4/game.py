import random


def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:  #if no ValueError
            if n > 0:
                break
    game(random.randint(1, n))


def game(i):
    while True:
        try:
            ans = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if ans > i:
                print("Too large! ")
            elif ans < i:
                print("Too small! ")
            elif ans == i:   #cannot use else because user may get it right on first try. no conditions for ans==i, only else:
                print("Just right! ")
                break


main()