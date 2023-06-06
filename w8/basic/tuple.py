def main():
    student = get_student()  #student is a tuple here. very similar to a list, just that tuples are immutable
    print(f"{student[0]} is in {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)    #returning a single tuple, with two values inside.
#brackets are for tuples, [name, house] to return a list


if __name__ == "__main__":
    main()