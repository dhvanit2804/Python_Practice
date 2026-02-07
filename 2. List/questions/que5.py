'Reverse a list without using reverse() or slicing.'

elements = [89, 55, 74, 75, 58]

reversed_list = []

for i in elements:
    reversed_list = [i] + reversed_list

print(reversed_list)
