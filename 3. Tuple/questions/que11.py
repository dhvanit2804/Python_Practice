'Given a tuple of numbers, create a new tuple containing only the even numbers.'

t = (87, 75, 78, 72, 88, 92, 98, 66, 74, 12, 26)

l = []

for i in t:
    if i % 2==0:
        l.append(i)

even_tuple = tuple(l)
print(even_tuple)