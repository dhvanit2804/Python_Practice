'Remove duplicate elements from a list using a set.'

s = {10, 20, 30, 40, 10, 20, 50}

s1 = set()

for num in s:
    if num not in s1:
        s1.add(num)

print(s1)