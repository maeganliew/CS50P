import sys

count = 0

if len(sys.argv) != 2:
    sys.exit("Invalid number of arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("not a python file")

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if not line.isspace() and not line.strip().startswith("#"):
                count += 1
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(count)