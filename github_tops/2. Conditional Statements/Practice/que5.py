'''Grade Calculator
Write a program to input marks of a student and display the grade according to the following:

90–100 → A
80–89 → B
70–79 → C
60–69 → D
below 60 → F'''

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Your Grade is:", grade)