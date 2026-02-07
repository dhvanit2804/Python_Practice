'Remove duplicate elements from a list.'

numbers = [10, 10, 20, 30, 30, 40, 50, 50]

num = []

for n in numbers:
    if n not in num:
        num.append(n)

print(num)