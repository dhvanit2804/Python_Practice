'Display only those characters which are present at an even index number in given string.'

string = "pynative"

for i in range(0, len(string) - 1, 2):
    print(string[i])

print(string[::2])