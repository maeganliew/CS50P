#operator overloading. few definitions for the same operator
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"There is {self.galleons}g, {self.sickles}s, {self.knuts}k"

    #to join harry and weasly's vault
    def __add__ (self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)   #returning a new Vault. the result of "adding" two vaults together


harry = Vault(100, 0, 50)
weasly = Vault(0, 100, 50)
total = harry + weasly   #when user overloads the operator(i.e. using it other than adding integers, Python will auto call the __add__ method)


print(total)