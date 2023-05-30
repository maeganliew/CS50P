import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"^.+src=\"https?://(?:www.)?youtube.com/embed/([0-9a-z]+)\".+$", s, re.IGNORECASE)
    if match:
        url = "https://youtu.be/" + match.group(1)
        return url
    else:
        return None


if __name__ == "__main__":
    main()