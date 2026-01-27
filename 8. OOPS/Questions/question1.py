'''Create a Rectangle class with attributes length and width. 
Add methods to calculate area and perimeter.'''

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(10, 20)
print(r.area())
print(r.perimeter())