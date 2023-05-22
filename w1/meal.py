def main():
    time = input("What time is it? ")
    num = convert(time.replace("a.m.", "").replace("p.m.", ""))
    if 7.0 <= num <= 8.0:
        if time.endswith("p.m."):
            print("", end="")
        else:
            print("breakfast time")

    elif 12.0 <= num <= 13.0 or (0.0 <= num-12 <= 1.0 and time.endswith("p.m.")):
        print("lunch time")
    elif 18.0 <= num <= 19.0 or (6.0 <= num <= 7.0 and time.endswith("p.m.")):
        print("dinner time")
    else:
        print("", end="")


def convert(n):
    a, b = n.split(":")
    number = float(a) + float(b)/60.0
    return number


if __name__ == "__main__":
    main()