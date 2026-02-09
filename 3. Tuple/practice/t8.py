'Count how many times an element appears in a tuple'

numbers = (10, 10, 20, 30)
n = []

for num in numbers:
    if num not in n:
        n.append(num)
        count = numbers.count(num)
        print(f"{num} appears {count} times")