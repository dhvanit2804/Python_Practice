'Count how many times an element appears in a list.'

numbers = [10, 20, 30, 40, 10, 20]
n = []

for i in numbers:
    if i not in n:
        n.append(i)
        count = numbers.count(i)
        print(f'{i} appears {count} times')