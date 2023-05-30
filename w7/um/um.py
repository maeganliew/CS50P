import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    s = s.lower()
    #edge case, ending with "um" for loop cannot detect
    if s.endswith("um"):
        count += 1
    if s.startswith("um") and len(s) != 2:
         count += 1
    for i in range(len(s)-4):
            if s[i+2]=="u" and s[i+3]=="m" and not s[i+1].isalpha() and not s[i+4].isalpha():
                count += 1
    return count


if __name__ == "__main__":
    main()