'Create a class Student that takes name and age as input and has a method display() to show details.'

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The Name of student is : {self.name}")
        print(f"The Age of student is : {self.age}")

name = input("Enter a name: ")
age = int(input("Enter a age: "))

s = Student(name, age)
s.display()