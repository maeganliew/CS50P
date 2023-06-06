#class methods
#not an instance method that has access to self, but it does know what class has inside
#no __init__ function. that is to instantiate multiple objects(like creating different students)
#but sorting hat only has one. instantiating sorting hat is like molding(creating) different sorting hats to sort a house for the student

import random

class Hat:
    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    @classmethod
    #cls referring to current class
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")