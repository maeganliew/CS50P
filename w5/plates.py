def main():
    text = input("Plate: ")
    if is_valid(text):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    for c in s:
        if c in [".", " ", "!"]:
            return False
    for i in range(len(s) - 1):
        if s[i].isnumeric() and s[i+1].isalpha():
            return False
    if not s[0].isalpha() or not s[1].isalpha:
        return False
    else:
        return True


if __name__ == "__main__":
    main()