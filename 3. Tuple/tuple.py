'What is Tuple in Python ?'
'''A tuple is a collection type in Python that is similar to a list but with an 
important difference: tuples are immutable. This means once a tuple is created, 
you cannot modify its elements, unlike lists, which are mutable'''


t = (1, 2, 10, 20, 1.1, 2.2, "tops", [100, 200, 300], True, "python", 100, 200, "java")

print(t.count(1))
print(t.index('java'))
print(t[7])
# print(t[::-1])
t[7].append(400)
print(t)

for i in t:
    print(i)

print(300 in t)
print(t[7][2])