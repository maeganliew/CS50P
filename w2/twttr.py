text = input("Input: ")

vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
print("Output: ", end="")

for char in text:
    if char in vowel:
        continue
    else:
        print(char, end="")
print()