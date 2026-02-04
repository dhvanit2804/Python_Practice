'''Basic Class Creation

Create a Car class with attributes like brand, model, and year. Add a method to display car information.'''

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("\n-- Car Information ---")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")

c = Car("Toyota", "Fortuner", 2025)
c.display()