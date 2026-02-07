'What is a List in Python?'
'''A list in Python is an ordered, mutable (changeable) collection that can store multiple items in a single variable.
Lists can contain different data types like integers, strings, floats, and even other lists.'''

marks = [94.4, 88.7, 76.5, 82.3, 91.0]
print(marks)
print(type(marks))

fruits = ['Mangos', 'Apple', 'Banana']
print(fruits)
print(type(fruits))

fruits[0] = "Orange"
print(fruits)

if 94.4 in marks:
    print("Yes")
else:
    print("No")

for mark in marks:
    print(mark)