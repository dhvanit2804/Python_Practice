'Remove duplicate elements from a list.'

numbers = [10, 10, 20, 30, 30, 40, 50, 50]

num = []

for i in numbers:
    if i not in num:
        num.append(i)

print(num)