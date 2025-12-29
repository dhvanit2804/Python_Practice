'''
Used to compare object memory locations.

Operator	Example	    Output
is	        x is y	    True if both refer to same object
is not	    x is not y	True if not same object
'''

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same object)
print(x is z)      # False (different objects)
print(x is not z)  # True
