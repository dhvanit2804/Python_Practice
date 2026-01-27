'''Create a Student class with attributes name, roll_no, and marks. 
Add a method to display student details and check if the student passed (marks >= 40).'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Roll No: {self.roll_no}")
        print(f"Student Marks: {self.marks}")

    def isPassed(self):
        return "Pass" if self.marks >= 40 else "Fail"
    
s = Student("Dhvanit", 81, 65)
s.display_info()
print(s.isPassed())