'Create a class Circle with a constructor that accepts radius and a method get_area() using πr².'

import math

class Circle:

    def __init__(self, radius):
        self.r = radius

    def get_area(self):
        return math.pi * self.r ** 2
    
r = float(input("Enter the radius of circle: "))
c = Circle(r)

print(f"Area Of Circle: {c.get_area():.2f}")