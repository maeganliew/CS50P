while True:
    try:
        num = int(input("What's x? "))
    except ValueError:
        print("Invalid Value")
    else:    #if no ValueError is catched, break the while loop and stop prompting user for input
        break
print(f"x is {num}")



#compact
def main():
    x = get_int("What's x? ")  #passing the question to be asked, can change name of variable/question here
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass  #ignoring the ValueError, continue prompting input without showing user the error message