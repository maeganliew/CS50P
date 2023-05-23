while True:
    try:
        text = input("Fraction: ")
        x, y = text.split("/")
        x, y = int(x), int(y)
    except ValueError:
        pass
    else:
        if x>y or y==0:
            continue
        break

percentage = x/y*100
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage:.0f}%")