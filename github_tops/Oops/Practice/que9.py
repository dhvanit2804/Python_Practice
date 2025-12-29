'Create a class Person that initializes with name and age, and has a method is_adult() that returns True if age ≥ 18.'

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18
    
p1 = Person("Dhvanit", 21)
p2 = Person("Ravi", 16)

print(f"{p1.name} is adult? {p1.is_adult()}")
print(f"{p2.name} is adult? {p2.is_adult()}")