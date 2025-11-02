'Create a class Employee with a method set_data() to assign values and show_data() to display them.'

class Emplooye:

    def set_date(self, name, age, role):
        self.n = name
        self.a = age
        self.r = role

    def show_data(self):
        print(f"The Name of Employee: {self.n}")
        print(f"The Age of Employee: {self.a}")
        print(f"The Role of Employee: {self.r}")

e = Emplooye()
e.set_date("Dhvanit", 21, "Python Developer")
e.show_data()