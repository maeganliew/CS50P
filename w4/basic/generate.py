#function takes in a list as argument, chooses a random element of the list
import random
print(random.choice(["apple", "orange"]))

from random import choice
print(choice(["1", "2"]))



#generates a random number between the range given
print(random.randint(1, 10))   #1-10 inclusive


#shuffles elements in a list
cards = ["a", "b", "c", "d", "e"]
random.shuffle(cards)     #does not return a value! shuffles the list in place
print(cards)