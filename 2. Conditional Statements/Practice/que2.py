'''Even or Odd
Write a program to check whether a given number is even or odd.'''

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even number.")
else:
    print(f"{number} is odd number")