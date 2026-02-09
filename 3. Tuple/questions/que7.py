'Convert a tuple into a list, modify one element, then convert it back into a tuple.'

t = (1, 2, 10, 20, 1.1, 2.2, "tops", [100, 200, 300], True, "python", 100, 200, "java")

l = list(t)

l.remove(200)
print(l)

t1 = tuple(l)
print(t1)