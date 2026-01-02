'Count how many digits are in a number'

numbers = input("Enter a number: ")
count = 0

for digit in numbers:
    count += 1

print("Number of digits:", count)