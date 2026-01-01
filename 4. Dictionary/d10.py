'''Count the frequency of characters in a string
"programming"'''

string = "programming"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)