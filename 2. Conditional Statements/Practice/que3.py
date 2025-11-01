'''Largest of Two Numbers
Write a program to find the largest of two numbers entered by the user.'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1>num2:
    print(f"{num1} is greater")
else:
    print(f"{num2} is greater")