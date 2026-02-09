'''Write a program to merge two dictionaries.
If a key exists in both, add their values.'''

d1 = {"a":10, "b":15}
d2 = {"b":10, "c":30}

result = d1.copy()

for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)