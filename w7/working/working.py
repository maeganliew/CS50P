import re
import sys


def main():
    print(convert(input("Hours: ")))

#(9)(:)?(30)?  (AM)?  to   (5)(:)?(30)? (PM)
#((?:[0-5])(?:\d)) is to check whether minutes is >60 (first digit can only be 0-5)
def convert(s):
    match = re.search(r"^(\d+)(\:)?((?:[0-5])(?:\d))? (AM|PM) to (\d+)(\:)?((?:[0-5])(?:\d))? (AM|PM)$", s)
    if match:
        #if AM set has colon
        if match.group(2):
            am = timing(match.group(4), match.group(1), match.group(3))
        else:
            am = timing(match.group(4), match.group(1))

        #if PM set has colon
        if match.group(2):
            pm = timing(match.group(8), match.group(5), match.group(7))
        else:
            pm = timing(match.group(8), match.group(5))
        return f"{am} to {pm}"
    else:
        raise ValueError


#default variable must be placed last. y="00"
def timing(status, x, y="00"):
    #edge case 12am and 12pm
    if int(x) == 12:
        x = str(int(x) - 12)
    if status == "AM":
        x = x.rjust(2, "0")
    else:
        x = str(int(x) + 12)
    return f"{x}:{y}"


if __name__ == "__main__":
    main()