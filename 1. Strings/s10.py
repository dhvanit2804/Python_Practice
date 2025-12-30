'''Find the first non-repeating character
Input: "swiss"
Output: "w"'''

s = "swiss"
char_count = {}

for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1

for ch in s:
    if char_count[ch] == 1:
        print(f"The first non-repeating character is: {ch}")
        break
else:
    print("No non-repeating character found.")