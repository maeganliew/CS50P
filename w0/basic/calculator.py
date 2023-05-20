x = int(input("x: "))
y = int(input("y: "))

z = x + y  #this operation will concatenate the strings, if you want to do math operation need to typecast. input functions will return strings

print(f"{z:,}")  #prints 1,000 instead of 1000

print(f"{z:.2f}")  #sets z to a two dec floating value