'Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.'

sentence = "Learning Python is fun!"
vowel = "aeiou"
count = 0

for char in sentence.lower():
    if char in vowel:
        count += 1

print(f"Number of vowels: {count}")