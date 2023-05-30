import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    count = 0
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):   #if ip is in the right format
        num_list = ip.split(".")
        for num in num_list:
            if int(num) in range (0, 255):
                count += 1
        if count == 4:
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    main()