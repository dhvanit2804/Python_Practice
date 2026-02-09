'''Add a new key "city" with value "Delhi" to this dictionary:

person = {"name": "Rahul", "age": 25}'''

person = {"name": "Rahul", "age": 25}
person["city"] = "Delhi"
print(person)

'Remove the key "age" from the dictionary above.'

person.pop('age')
print(person)