'''map() function is a built-in function that allows you to apply a specified 
function to all the items in an iterable (like a list, tuple, or any other 
iterable) and return a new iterable (usually a map object) with the results'''

l1 = [1, 2, 3, 4, 5]

def square(n):
    return n*n

l2 = list(map(square, l1))

print(l2)