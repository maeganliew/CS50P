def main():
    x = int(input("Number: "))
    if f_even(x):
        print("Num is even")
    else:
        print("Num is odd")

def f_even(n):
    return True if n % 2 == 0 else False   #put everything into one line
    return n % 2 == 0   #the statement itself is having True/False values, depending of value of n

main()