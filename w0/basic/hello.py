#get input. #remove white spaces AND capitalise every word
name = input("What's your name? ").strip().title()

#splitting strings
first, last = name.split(" ") #split into first and last name, separated by space


print("hello,", name)

#format string (f formats string to allow plugged in variables)
print(f"hello, {name}")

#to print literal double quuotes, use single quotes in print function
print('hello, "friend"')

#escape characters (if die die want use double quotes)
print("hello, \"friend\"")