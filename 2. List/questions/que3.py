'Find the largest and smallest number in a list.'

elements = [89, 55, 74, 75, 58]

largest = elements[0]
smallest = elements[0]

for i in elements:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest Number in List: ",largest)
print("Smallest Number in List: ",smallest)