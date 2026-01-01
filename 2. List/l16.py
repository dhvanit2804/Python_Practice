'Remove duplicate elements from a list.'
numbers = [10, 20, 30, 40, 10, 20]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)