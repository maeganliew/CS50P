import requests, sys, json


def main():
    n = getfloat()
    price = getprice()
    total = format(n*price)
    print(f"${total}")


def getfloat():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return n


def getprice():
    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    #remember to strip the front&end quote symbols, and remove comma !!
    rate = price["bpi"]["USD"]["rate"].removeprefix('"').removesuffix('"').replace(",", "")
    rate = float(rate)
    return rate


def format(total):
    front = int(total/1000)
    back = float(total%1000)
    return(f"{front},{back:.4f}")


main()