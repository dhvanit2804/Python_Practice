class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def start(self):
        print(f"The {self.color} car is starting.")

car = Car("red", 120)
car.start()

a = 10      # int
b = 2.5     # float

c = a + b

print(c)
print(type(c))