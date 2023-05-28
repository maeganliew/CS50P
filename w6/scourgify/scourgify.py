import sys, csv

data = []   #list of dicts

def main():
    check_arg()
    read_file()
    write_file()


def check_arg():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")


def read_file():
    try:
        with open(sys.argv[1], "r") as inputfile:
            reader = csv.DictReader(inputfile)
            for row in reader:   #each row is read as a dict
                last, first = row["name"].split(",")    #separate first name and last name
                data.append({"first": first.strip(), "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit("Could not open first file provided")


def write_file():
    with open(sys.argv[2], "a") as outputfile:
        #line 31 aand 32 is to write the header(list) first
        writer = csv.writer(outputfile)
        writer.writerow(["first", "last", "house"])
        writer = csv.DictWriter(outputfile, fieldnames=["first", "last", "house"])
        for row in data:   #iterating through each row(dict) in contents
            writer.writerow(row)


if __name__ == "__main__":
    main()