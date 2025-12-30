'''Count frequency of each character in a string
Input: "programming"'''

s = "programming"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:")
for key in freq:
    print(key, ":", freq[key])