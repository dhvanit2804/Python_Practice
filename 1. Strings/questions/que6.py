'Check if two strings are anagrams - Determine if two strings contain the same characters in different orders.'

s1 = input("Enter a string 1: ")
s2 = input("Enter a string 2: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not anagram")