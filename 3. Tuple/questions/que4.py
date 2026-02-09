'Find the length of a tuple.'

t = (1, 2, 10, 20, 1.1, 2.2, "tops", [100, 200, 300], True, "python", 100, 200, "java")

count_len = 0

for i in t:
    count_len += 1

print(f"Length Of Tuple is : {count_len}")