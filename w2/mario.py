height = int(input("Height of block: "))


for i in range(height):
    m = height
    n = 0
    j = height
    for _ in range(height-1-i):
        print(" ", end="")
    while m > height-1-i:
        print("#", end="")
        m -= 1

    print(" ", end="")

    while j > height-1-i:
        print("#", end="")
        j -= 1
    for _ in range(height -1 -i):
        print(" ", end="")

    print()
    i+=1