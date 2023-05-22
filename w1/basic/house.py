name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":   # | means or in the match function
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  #case that is not handled
        print("Whooooo")