#inheritance. student and professor are both wizards, their class inherits the Wizard class
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        #"super" is referring to the parent class. in this case "Wizard"
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        self.subject = subject
        super().__init__(name)


wizard = Wizard("Dumbledore")   #not a student nor professor
student = Student("Harry", "Gryffindor")
professor = Professor("Snape", "Slytherin")