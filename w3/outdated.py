month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    m, d, y = get_date()
    m = str(m).rjust(2, "0")  #typecast str, pad with zero values
    d = str(d).rjust(2, "0")

    print(f"{y}-{m}-{d}")


def get_date():
    while True:
        text = input("Date: ")
        if "/" in text:   #date with slash format
            m, d, y = text.split("/")
            if not m.isalpha():
                m, d, y = int(m), int(d), int(y)
                if (0 < d < 32) and (0 < m < 13):   #check for valid date
                    return m, d, y
        else:
            m, d, y = text.split(" ")
            if "," in d:
                d = d.removesuffix(",")  #remove the comma coming with date
                if d.isnumeric():
                    d = int(d)
                    if (m in month) and (0 < d < 32):
                        m = month.index(m) + 1
                        return m, d, y

main()