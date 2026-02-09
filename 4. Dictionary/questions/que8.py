'''iterate through this dictionary and print keys and values in this format:

math -> 85
science -> 90'''

marks = {"math": 85, "science": 90, "English": 70}

for i in marks:
    print(f"{i} -> {marks[i]}")