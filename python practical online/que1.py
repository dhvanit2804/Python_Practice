'''Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.'''

def multiplication_or_sum(a, b):

    product = a * b

    if product <= 1000:
        return product
    else:
        return a + b

result = multiplication_or_sum(30, 30)
print(f"The Result is {result}")

result1 = multiplication_or_sum(40, 30)
print(f"The Result is {result1}")