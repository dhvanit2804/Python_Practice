my_dict = {
    "name": "Dhvanit",
    "age": 21,
    "city": "Ahmedabad"
}

print(my_dict)
print(my_dict.get("name"))

my_dict['email'] = "dhvanit@123gmail.com"
print(my_dict)

my_dict['age'] = 22
print(my_dict)

del my_dict['city']
print(my_dict)

new_info = {'city':"Ahmedabad", "clg":"Rb"}

my_dict.update(new_info)
print(my_dict)