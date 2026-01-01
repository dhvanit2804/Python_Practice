'Count how many keys are in a dictionary.'

student = {
    "name": "Dhvanit",
    "roll_no": 101,
    "course": "BCA",
    "semester": 6,
    "college": "Silver Oak University"
}

count = 0
for key, value in student.items():
    count += 1

print(count)