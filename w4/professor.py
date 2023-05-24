import random


def main():
    score = 0
    level = get_level()
    print()
    for _ in range(10):
        wrong = 0
        X = generate_integer(level)
        Y = generate_integer(level)
        for _ in range(3):
            ans = int(input(f"{X} + {Y} = "))
            if (ans == X+Y):
                score += 1
                break
            else:
                print("EEE")
                wrong += 1
        if wrong == 3:
            print(f"{X} + {Y} = {X+Y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n in [1,2,3]:
                return n


def generate_integer(level):
    if level == 1:
        return(random.randint(0, 9))   #must include zero!
    elif level == 2:
        return(random.randint(10, 99))
    else:
        return(random.randint(100, 999))


if __name__ == "__main__":
    main()