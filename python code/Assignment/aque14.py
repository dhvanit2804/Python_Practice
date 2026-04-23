'Write a program to display all keys and values of a dictionary using loop'

my_dict = {
    "name": "Dhvanit",
    "age": 21,
    "city": "Ahmedabad"
}

for key, values in my_dict.items():
    print(f"{key}: {values}")