'''Convert two lists into a dictionary:

keys = ["name", "age", "city"]
values = ["Anita", 22, "Mumbai"]'''

keys = ["name", "age", "city"]
values = ["Anita", 22, "Mumbai"]

student = dict(zip(keys, values))

print(student)