'''Create:

Employee (base)
FullTimeEmployee
PartTimeEmployee

Each has:
calculate_salary()
Different logic for each type.'''

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmplooye(Employee):

    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmplooye(Employee):

    def __init__(self, name, emp_id, hours, rate):
        super().__init__(name, emp_id)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate * 30
    
class Intern(Employee):

    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
    

f = FullTimeEmplooye("Dhvanit", 28, 20000)
print(f.calculate_salary())

p = PartTimeEmplooye("Meet", 5, 10, 40)
print(p.calculate_salary())

i = Intern("Rahul", 29, 5000)
print(i.calculate_salary())