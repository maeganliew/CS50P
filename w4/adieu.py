names = []

def main():
    while True:
        try:
            text = input("Name: ")
            names.append(text)
            #ft_print(names)
        except EOFError:
            print()
            ft_print(names)
            break


def ft_print(list):
    n = len(list)
    print("Adieu, adieu, to ", end="")
    if n == 1:
        print(list[0])
    elif n == 2:
        print(f"{list[0]} and {list[1]}")
    else:
        for i in range(n-1):
            print(f"{list[i]}, ", end="")
            i += 1
        print(f"and {list[n-1]}")


main()