'Check whether a given element exists in a tuple.'

t = (1, 2, 10, 20, 1.1, 2.2, "tops", [100, 200, 300], True, "python", 100, 200, "java")

element = "python"

if element in t:
    print("Element is avilable in tuple")
else:
    print("Element is not avilable in tuple")