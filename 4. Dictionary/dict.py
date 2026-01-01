'What is Dictionary in Python ?'
'''A dictionary is a collection of key-value pairs, where each key is unique, and 
each key is associated with a value. Dictionaries are unordered, mutable, and 
indexed by keys. They are defined using curly braces {} or the dict() constructor.'''

student = {
    'name': 'Dhvanit Parate',
    'age': 21,
    'courses': ['Frontend', 'Backend'],
    'languages': ['Python', 'JavaScript']
}

print(student)
print(type(student))

print('\nAccessing Values:')
print(student['name'])          # Accessing value using key
print(student.get('age'))      # Accessing value using get() method 

print(student['courses'][0])  # Accessing nested value