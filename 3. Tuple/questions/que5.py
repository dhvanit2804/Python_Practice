'Count how many times a specific value appears in a tuple.'

t = (1, 2, 10, 20, 1.1, 2.2, "tops", [100, 200, 300], True, "python", 100, 200, "java")

count = 0

for i in t:
    if i == 1:
        count += 1

print(f"The Value Of 1 appers in tuple {count} times")