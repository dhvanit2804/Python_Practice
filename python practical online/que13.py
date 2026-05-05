'Iterate through a given list of numbers and print only those numbers which are divisible by 5.'

num_list = [10, 20, 33, 46, 55]
l = []

for i in num_list:
    if i % 5 == 0:
        l.append(i)

print(f"Divisible by 5: {l}")