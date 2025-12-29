class Car:
    wheels = 4 # Class Attribute (shared by all instances)

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels)
print(car2.wheels)