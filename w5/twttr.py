def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(str):
    copy = ""
    for c in str:
        if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:     #str.replace will not replace original string, need to store in new variable
            continue
        else:
            copy += c  #concatenate all non-vowel characters into copy
    return copy


if __name__ == "__main__":
    main()