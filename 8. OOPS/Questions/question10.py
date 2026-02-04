'''Create a base class Animal with methods speak() and move(). Create derived classes Dog, Cat, and Bird that override these methods.'''

class Animal:

    def speak(self):
        print("Animal Speaking")

    def move(self):
        print("Animal Move")

class Dog(Animal):

    def speak(self):
        print("Dog Barks")

    def move(self):
        print("Dog Runs")

class Cat(Animal):

    def speak(self):
        print("Cat Meows")

    def move(self):
        print("Cat Walks")

class Bird(Animal):

    def speak(self):
        print("Bird Chirps")

    def move(self):
        print("Bird Flies")

d = Dog()
d.speak()
d.move()

c = Cat()
c.speak()
c.move()

b = Bird()
b.speak()
b.move()