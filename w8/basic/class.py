#invent a new datatype called student. Student works as a function as well
#function in classes are called methods
#every method takes in default arg "self", gives user access to current object
class Student:
    def __init__(self, name, house, patronus):    #passing in variables to customise the contents of objects
        #line 7 and 8 is no longer needed because the setter getter already checks the house input
        #if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            #raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus


    def __str__(self):     #string method. used when you want to print classes out as strings (if str method not used, the memory of the object will be printed instead of the content of the object)
        return f"{self.name} is in {self.house}"


    #can also write a separate function outside of class, but better here cuz getting info of student is also Student related. just a matter of design
    @classmethod
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)   #passing arguments to __init__ to instantiate an object(a new student)


    #Getter. method in class that gets some value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    @property
    def house(self):
        return self._house     #instance variable is now student._house (student.house is a "path" to go into the house property)

    #Setter. sets value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


    #self invented function. if want to call, object.method()
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Stag emoji"
            case "Otter":
                return "Otter emoji"
            case _:
                return "Default charm"



def main():
    student = Student.get_student()
    # this line ot manually changing the values can be prevented by the getter and setter mechanism.
    # each time someone tries to change value by escaping the checks in __init__ (checks only run when first instantiating object), student.house will go into the house method
    #student.house = "IPOH"
    print(student)
    #print(f"Expecto Patronum!, {student.charm()}")


if __name__ == "__main__":
    main()