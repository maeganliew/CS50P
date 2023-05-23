dict = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1


for i in sorted(dict):    #sort the dict in alpha order
    print(f"{dict[i]} {i}")