'Print only the keys whose value is greater than 50'

data = {
    'a': 45,
    'b': 67,
    'c': 23,
    'd': 89,
    'e': 12,
    'f': 56
}

for key, value in data.items():
    if value > 50:
        print(f"{key} = {value}")