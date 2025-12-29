class Person:
    fname = ""
    lname = ""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def showName(self):
        print(f"First Name: {self.fname} And Last Name: {self.lname}")

class Employee(Person):

    sno = 0
    def __init__(self, fname, lname, sno):
        Person.__init__(self,fname, lname)
        self.sno = sno

    def showEmployee(self):
        self.showName()
        print(f"Staff Number : {self.sno}")

b = Person("Dhvanit", "Parate")
a = Employee("Dhvanit","Parate",28)

a.showEmployee()