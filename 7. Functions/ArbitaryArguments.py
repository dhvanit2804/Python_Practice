'What is Arbitrary Arguments in Python Functions?'
'Arbitrary Arguments allow you to pass a variable number of arguments to a function. '
'In Python, this is done using the *args and **kwargs syntax.'

def test(a, b, c, *d, **e):
    print(f"A : {a}, B : {b}, C : {c}, D : {d}, E : {e}")

test(1, 2, 3, 4, 5, 6, 7, 8,x=10, y=20, z=30)

# Example 2: Calculate sum of all numbers
# def calculate_sum(name, *numbers):
#     total = sum(numbers)
#     print(f"{name}, the sum of {numbers} is: {total}")

# calculate_sum("Student", 10, 20, 30, 40, 50)