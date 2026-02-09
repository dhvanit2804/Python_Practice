'Find the maximum and minimum values in a tuple of numbers.'

t = (10, 20, 30, 40, 50, 60, 80)

maximum = t[0]
minimum = t[0]

for i in t:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(f"Maximum Value Of tuple: {maximum}")
print(f"Minimum Value Of tuple: {minimum}")