import re

re.match(pattern, string, flags=0)   #auto start matches from start of input(input[0])

re.fullmatch(pattern, string, flags=0)  #auto start matches start and end of string. similar to ^$ in pattern

re.split(pattern, string, maxsplit=0, flags=0)

#search for multiple copies of the same pattern
re.findall(pattern, string, flags=0)