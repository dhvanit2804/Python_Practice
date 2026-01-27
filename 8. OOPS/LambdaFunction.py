'''Lambda functions are short functions that can have any number of 
arguments but only one expression. They are often used when a 
small, throwaway function is needed.'''

double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x>y else y


print(double(5))
print(add(5, 12))
print(max_value(55, 87))