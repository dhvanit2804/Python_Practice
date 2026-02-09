'''Given a dictionary:
marks = {"math": 85, "science": 90, "english": 78}
Find the subject with the highest marks.'''

marks = {"math": 85, "science": 90, "english": 78}

subject = max(marks, key=marks.get)

print(subject, marks[subject])