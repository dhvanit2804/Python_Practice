'Find the index of an element in a tuple, handling the case where it does not exist.'

t = (10, 20, 30, 40)

element = 30

try:
    index = t.index(element)
    print(f"Index: {index}")
except ValueError:
    print("Element not found")