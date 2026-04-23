'Write a program to print the factorial of a number using loops'

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i

print(factorial)