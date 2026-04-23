class Animal:
    def speak(self):
        print("Animal Makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog Makes Sound")

d = Dog()
d.speak()
d.bark()