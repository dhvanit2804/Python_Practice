class Student:

    def getdata(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def putData(self):
        print(f"First Name : {self.fname}")
        print(f"Last Name : {self.lname}")

s1 = Student()
s1.getdata("Dhvanit", "Parate")
s1.putData()