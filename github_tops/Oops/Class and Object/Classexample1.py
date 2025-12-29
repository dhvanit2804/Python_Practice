class Person:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def greet(self):
        return f"Hello My Name is {self.name} and i am {self.age} years old my subject is {self.subject}"

p = Person("Dhvanit",21,"Python")

print(p.name)
print(p.greet())