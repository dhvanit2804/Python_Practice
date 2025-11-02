'Create a class Car with attributes brand and color. Create an object and print its attributes.'

class Car:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def show(self):
        print(f"The Car Brand is {self.brand} and Car Color is {self.color}") 

c = Car("Toyota", "Black")
c.show()