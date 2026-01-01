'Print all keys and values using a loop.'

student = {
    "name": "Dhvanit",
    "roll_no": 101,
    "course": "BCA",
    "semester": 6,
    "college": "Silver Oak University"
}

print("Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")