import re

name = input("What's your name? ").strip()

# (text) is whatever text you wanna capture from user's input. groups
# matches = anything found between pattern and input
# , *   means comma+space(zero or more). the asterisk is behind the space

#(:=)assigning return value of re.search to matches AND asking boolean if there is matches(found string in pattern format)
if matches := re.search(r"^(.+), ?(.+)$", name):
    last, first = matches.groups()      #finding groups(surrounded by brackets) in matches
    name = f"{first} {last}"            #changing "Malan, David" to "David Malan"

    #line 11 same as
    last = matches.group(1)
    first = matches.group(2)     #theres a difference between group/groups

    #or
    name = matches.group(2) + " " + matches.group(1)
