'''Smallest of Three Numbers
Write a program to find the smallest of three numbers entered by the user.'''

a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
c = int(input("Enter a num: "))

if a < b and a < c:
    print(f"Smallest Number is {a}")
elif b < c:
    print(f"Smallest Number is {b}")
else:
    print(f"Smallest Number is {c}")