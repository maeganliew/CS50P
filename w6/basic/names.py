name = input("What's your name?  ")


with open("names.txt", "a") as file:    #open the file in append mode. "w" is in writing mode, everytime opening the file will overwrite the contents
    file.write(f"{name}\n")


with open("names.txt", "r") as file:
    #line = file.readlines()
    for line in sorted(file, reverse=True):     #by default reverse=False, if want to sort in descending order reverse=True 
        print("Hello", line.strip())  #each line is with a new line already(in the file),
