'Reverse a number using a loopReverse a number using a loop'
numbers = int(input("Enter a number: "))
reverse = 0

while numbers > 0:
    digit = numbers % 10
    reverse = reverse * 10 + digit
    numbers = numbers // 10

print("Reversed number:", reverse)