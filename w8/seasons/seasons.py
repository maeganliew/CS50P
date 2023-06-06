from datetime import date
import sys, re, inflect

p = inflect.engine()  #a part of inflect package

def main():
    date = get_date()
    print(calculate(date))


def get_date():
    date = input("Date of birth: ")
    match = re.search(r"^\d\d\d\d-\d\d-\d\d$", date)
    if match:
        return date
    sys.exit("Invalid Date Format")


#remember to not name arguments "date". its the name of the class
def calculate(input):
    year, month, day = input.split("-")

    birth = date(int(year), int(month), int(day))    #instantiating a new object for birth date
    current = date.today()  #returns the date object?
    diff = current - birth     #returns number of days

    minutes = int(diff.total_seconds() / 60)
    string = p.number_to_words(minutes, andword="").capitalize() + " minutes"
    return string


if __name__ == "__main__":
    main()