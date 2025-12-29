'''Positive or Negative
Write a Python program to check whether a number entered by the user is positive, negative, or zero.'''

num = int(input("Enter a num: "))

if num >= 0:
    print("Number is Positive")
elif num <= 0:
    print("Number is negative")
else:
    print("zero")