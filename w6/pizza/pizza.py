import sys, csv
from tabulate import tabulate

content = []   #list of lists
table = []    #list of lists
header = []


def main():
    check_arg()
    read_file()
    print_table()


def check_arg():
    if len(sys.argv) != 2:
        sys.exit("Invalid number of arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")


def read_file():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)   #reads every row as a list
            for row in reader:
                content.append(row)  #row is sublist, added to mainlist(content)
    except FileNotFoundError:
        sys.exit("File not found")


def print_table():
    for list in content[1:]:   #iterating through every sublist in mainlist, skipping the header
        table.append(list)
    print(tabulate(table, headers=content[0], tablefmt="grid"))


if __name__ == "__main__":
    main()