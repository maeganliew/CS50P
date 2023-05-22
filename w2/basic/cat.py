for i in [0, 1, 2]:   #square bracket means a list in python
    print("meow")


print("meow\n" * 3, end = "")


while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):  #avoid creating another variable just to count
    print("meow")