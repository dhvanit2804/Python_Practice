'Count vowels and consonants - Count the number of vowels and consonants in a given string.'

s = input("Enter string: ")

vowel = 0
consonants = 0

for i in s:
    if i in 'aeiouAEIOU':
        vowel += 1
    elif i.isalpha():
        consonants += 1

print(vowel)
print(consonants)