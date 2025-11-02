'Create a class Rectangle with attributes length and width, and a method area() that returns the area.'

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

r = Rectangle(length, width)
r.area()