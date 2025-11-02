class Person:

    fname = ""
    lname = ""
    email = ""

    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def showDetails(self):
        print(f"Fname : {self.fname}")
        print(f"Lname : {self.lname}")
        print(f"Email : {self.email}")

fname = print(input("Enter the Fname :"))
lname = print(input("Enter the Lname :"))
email = print(input("Enter the Email : "))

p = Person(fname, lname, email)
p.showDetails()