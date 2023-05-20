def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(str1="world"):   #assign str1 value, if function is called without args then str1=world. like hello()
    print(f"Hello, {str1}")

main()  #this line is calling main. unlike in C, defining main in Python doesnt exactly mean calling it