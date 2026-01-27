'''Implement inheritance hierarchy:

Base class: Vehicle (brand, model, year)
Derived classes: Car (num_doors), Motorcycle (engine_cc)
Override display_info() method in each class'''

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Vehicle Info: {self.brand} {self.model}, Year: {self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Num Doors: {self.num_doors}"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Engine cc: {self.engine_cc}"
    
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 2019, 689)
print(car.display_info())
print(motorcycle.display_info())