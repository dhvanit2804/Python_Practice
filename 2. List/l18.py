'Find the second largest number in a list.'

numbers = [17, 18, 19, 20, 22, 24, 25]
n = max(numbers)
numbers.remove(n)
print(max(numbers))