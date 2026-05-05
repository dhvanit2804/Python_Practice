'Write a script that takes a list containing duplicate items and returns a new list with only unique elements.'

data = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = []

for i in data:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)