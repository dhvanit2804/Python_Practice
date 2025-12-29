'''Used to perform bit-level operations.

Operator	    Meaning	        Example	        Output
&	            AND	            5 & 3	        1
`	            `	            OR	            `5
^	            XOR	            5 ^ 3	        6
~	            NOT	            ~5	            -6
<<	          Left shift	    5 << 1	        10
>>	          Right shift	    5 >> 1	        2'''

a, b = 5, 3
print(a & b, a | b, a ^ b, ~a, a << 1, a >> 1)
