'''Count vowels in a string
Input: "education"
Output: 5'''

s = "Education"
count = 0

for ch in s.lower():
    if ch in 'aeiou':
        count+= 1

print(f"Number Of Vowels = {count}")