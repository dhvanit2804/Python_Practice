'''Check whether two strings are anagrams
Input: "listen", "silent"
Output: True'''

s1 = input("Enter a first string: ")
s2 = input("Enter a second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("String are anagrams")
else:
    print("Strings are not Anagrams")