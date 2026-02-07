'Remove duplicates - Remove duplicate characters from a string while preserving order.'

s = input("Enter a string: ")

result = ""

for i in s:
    if i not in result:
        result += i

print(result)