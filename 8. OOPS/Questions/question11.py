'Create a Person class with private attributes __age and __salary. Implement getter and setter methods with validation.'

class Person:

    def __init__(self, age, salary):
        self.__age = age
        self.__salary = salary

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary Cannot be negative")

p = Person(25, 10000)

print(p.get_age())
p.set_age(30)

p.set_salary(20000)

print(p.get_age())
print(p.get_salary())