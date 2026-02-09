'Find all even numbers from a tuple?'

numbers = (88, 87, 85, 81, 84, 54, 44)
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

print(even)