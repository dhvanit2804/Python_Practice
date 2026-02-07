'Count how many times a given element appears in a list.'

elements = [89, 55, 74, 75, 58, 89, 55]
element_to_count = 89
count = 0

for i in elements:
    if i == 89:
        count+=1

print(count)