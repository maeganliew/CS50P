def main():
    text = input("")
    print(convert(text))

def convert(str1):
    str2 = str1.replace(":)", "🙂").replace(":(", "🙁")
    return str2

main()