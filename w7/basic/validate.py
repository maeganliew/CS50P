import re

#SIDENOTE
#can use f" " for patterns, if want to check for specific variable inside input



email = input("What's your email? ").strip()

#re.search(pattern, input)   checks if input fullfill the pattern
# .+ means any char except a new line, by 1/more repetitions
# .+ is the same as ..*  (.* just means zero or more non-newline characters)
# \(escape characters) is used when literally matching "." instead of meaning:any char except newline
# r" " is to specify that this string should be treated as raw string(so that it doesnt begin an escape sequence)
# ^ and $ means user's input should start and end with .+@.+\.edu  (rejects input like: My email is mjw.liew@gmail.com)
if re.search(r"^.+@.+\.edu$", email):
    print("Valid1")


#[^@] means any characters BUT a @ sign(means @ cannot occur before the real @)
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid2")


#[ ] without ^ means a set of characters to allow
#[a-zA-z0-9] means any alphabet(whether uppercase/lowercase) or digits or underscores
if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9_]+\.edu$", email):
    print("Valid3")

#\w means alphabets(a/A),numbers and underscores, same as [a-zA-z0-9_]. "word" charaters
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid4")


#supports "list" of endings. the flag passed in will let the function ignore the case of user's input
if re.search(r"^\w+@\w+\.(edu|com|org|gov)$", email, re.IGNORECASE):
    print("Valid5")
#mjw.liew@gmail.com is not valid cuz the pattern does not support "." before "@". only \w characters


#a sub-pattern that may or may not be present
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|org|gov)$", email, re.IGNORECASE):
    print("Valid6")
# mjw.liew@cs50.gmail.com and mjw.liew@gmail.com are both valid. the additional (\w+\.) may/may not present cuz ? mark is added
