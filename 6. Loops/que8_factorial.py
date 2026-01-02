'Find the factorial of a number'

numbers = int(input("Enter a number: "))
factorial = 1

for i in range(1, numbers + 1):
    factorial = factorial * i
print(f"The factorial of {numbers} is {factorial}")