'Check if a string is a palindrome - Determine if a string reads the same forwards and backwards.'

s = input("Enter a string: ")

s1 = s[::-1]

if s == s1:
    print("String is palindrome")
else:
    print("String is not palindrome")