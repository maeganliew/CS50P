def main():
    while True:
        try:
            text = input("Fraction: ")
            num = convert(text)
            print(gauge(num))
            break
        except (ZeroDivisionError, ValueError):
            continue    #reprompt if got error


def convert(fraction):
    while True:
        try:
            X, Y = fraction.split("/")
            X, Y = int(X), int(Y)
            num = round((X/Y) *100)
            if X>Y:
                raise ValueError
            return num
        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()