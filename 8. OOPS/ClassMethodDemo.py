class Student:
    subject = "Python" # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_subject(cls):
        return cls.subject
    
    @classmethod
    def set_subject(cls, new_subject):
        cls.subject = new_subject

# Calling Class Method
print(Student.get_subject())

# Modifying
Student.set_subject("Java")
print(Student.get_subject())