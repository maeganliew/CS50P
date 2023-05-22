symbols = [".", " ", "!", ","]


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    for c in s:
        if c in symbols:
            return False

    i = 0
    while i < len(s) - 1:
        if s[i].isnumeric():
            if s[i+1].isalpha():
                return False
        i += 1

    if s[0].isalpha() or s[1].isalpha:   #idk whats wrong with   if s[0].isnumeric() or s[1].numeric:, return False
        return True
    else:
        return False


main()