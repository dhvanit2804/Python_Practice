'''Create a Circle class with attribute radius. 
Add methods to calculate area and circumference using @property decorator.'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
c = Circle(7)

print("Area: ",c.area)
print("Circumference: ",c.circumference)