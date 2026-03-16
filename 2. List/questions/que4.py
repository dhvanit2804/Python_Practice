'Count how many times a given element appears in a list.'

elements = [89, 55, 74, 75, 58, 89, 55]
elem_count = 89
count = 0

for i in elements:
    if i == elem_count:
        count += 1

print(count)