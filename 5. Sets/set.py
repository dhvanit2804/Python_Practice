'''set is an unordered collection of unique elements. It 
is a built-in data type that allows you to store multiple 
items in a single variable'''

s = {10, 20, "tops", True, "python", 1.1, 2.2, "java",10, 20, 1, 2, False, "testing"}
s1 = {1,2,3,4,5,6,7,8,9,10,"python"}

print(s)
s.add(100)
print(s)
print(s.difference(s1))
s.discard(1)
print(s)

'pop remove data from first'
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

s.remove(10)
print(s)

s2 = {1.1,2.2,3.3,4.4,5.5,6.6,7.7}
s.update(s2)
print(s)

print()