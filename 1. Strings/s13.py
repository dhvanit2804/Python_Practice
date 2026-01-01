'''Capitalize the first letter of every word
Input: "python is powerful"
Output: "Python Is Powerful"'''

s = "python is powerful"
words = s.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:])

print(f"Output: {" ".join(result)}")