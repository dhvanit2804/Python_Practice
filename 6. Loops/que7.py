'Check whether a number is Palindrome'

numbers = int(input("Enter a number: "))
original_number = numbers
reverse = 0

while numbers > 0:
    digit = numbers % 10
    reverse = reverse * 10 + digit
    numbers = numbers // 10
if original_number == reverse:
    print(f"{original_number} is a Palindrome")