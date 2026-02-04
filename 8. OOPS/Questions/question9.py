'''Create a Student class where each student has a name and grade, but all students share the same school name (class variable).'''

class Student:

    school_name = "Silver Oak"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print("\n--- Student Information ---")
        print(f"Name : {self.name}")
        print(f"Grade : {self.grade}")
        print(f"School Name : {Student.school_name}")

s = Student("Dhvanit", "A")
s.display()