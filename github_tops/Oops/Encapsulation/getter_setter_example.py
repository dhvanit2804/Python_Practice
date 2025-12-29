class Person:
    def __init__(self, name, age):
        #Private Attributes
        self.__name = name
        self.__age = age

    # Getter Method for name
    def get_name(self):
        return self.__name
    
    # Setter Method for name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name. Name Should be a non-empty string.")

    # Getter Method for Age
    def get_age(self):
        return self.__age

    # Setter Method for Age
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age. Age should be a non-negative integer.")

person = Person("Dhvanit",21)

print(person.get_name())
print(person.get_age())

person.set_name("Meet")
person.set_age(22)

print(person.get_name())
print(person.get_age())

person.set_name("")
person.set_age(-5)