def main():
    x = int(input("What is x: "))
    print(f"x square is {square(x)}")

def square(n):
    return n*n  
    return n**2   #two asterisks mean power ^
    return pow(n, 2)

main()