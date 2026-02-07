'Convert all lowercase letters to uppercase without using .upper()'

s = input("Enter a string: ")

result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(f"Uppercase string: {result}")