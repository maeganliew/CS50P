def main():
    hello("maegan")
    goodbye("maegan")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


#to prevent calling main function every time library is used in other files(calling unconditionally)
if __name__ == "__main__":
    main()