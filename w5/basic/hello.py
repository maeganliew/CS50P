def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(name="world"):    #if no user input
    return f"hello, {name}"


if __name__ == "__main__":
    main()