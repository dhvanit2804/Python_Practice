'''Used to combine conditional statements.

Operator	    Meaning	                    Example	                Output
and	        True if both are True	        (x > 5 and y < 10)	    True
or	        True if at least one is True	(x > 5 or y > 10)	    True
not	        Reverses result	not             (x > 5)	                False'''

x, y = 10, 5
print(x > 5 and y < 10)  # True
print(x > 5 or y > 10)   # True
print(not(x > 5))        # False
