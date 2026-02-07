'''Remove duplicate characters from a string
Input: "aabbccdde"
Output: "abcde"'''

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result+= ch

print(f"String After Removing Duplicates: {result}")