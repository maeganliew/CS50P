import re  #regular expressions library

url = input("Twitter URL: ").strip()

#substitutes the pattern into something else
# ori url: https://twitter.com/username
# yellow backslash is an escape character. if not putting \ the "." will mean all chars except new line
# tolerates http/https
# tolerates https://"www".twitter.com/username
# tolerates www.twitter.com/username   (without "http/https" protocol)
# (.+) at last is where username is captured


#if url= https://twitter.com/maeganliew,
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(matches.group(1))    #prints maeganliew

#first two groups already specifies (?:  ) which means group but DO NOT capture