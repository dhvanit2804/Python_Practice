'Find the longest word in a string'

s  = "The quick brown fox jumps over the lazy dog"
words = s.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)