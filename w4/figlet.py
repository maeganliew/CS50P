import pyfiglet, random, sys
from pyfiglet import Figlet

figlet = Figlet()

#if len(sys.argv) not in [1, 3]:   not sure why !=1 or != 3 doesnt work
    #sys.exit("Invalid usage")

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

else:
    sys.exit("Invalid usage")


text = input("Input: ")
print(figlet.renderText(text))