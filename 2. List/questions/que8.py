'Create a new list containing only even numbers from an existing list.'

numbers = [10, 13, 16, 21, 27, 22, 28, 31, 24, 34, 38]

num = []

for i in numbers:
    if i % 2 == 0:
        num.append(i)

print(num)