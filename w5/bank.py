def main():
    text = input("Greeting: ")
    print(f"${value(text)}")


def value(greeting):
    if greeting == "":
        return 100
    elif greeting[0] in ["h", "H"]:
        #start finding Hello from 0th to 5th char, if cannot find will return -1
        if greeting.rfind("Hello", 0, 5) != -1 or greeting.rfind("hello", 0, 5) != -1:
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()