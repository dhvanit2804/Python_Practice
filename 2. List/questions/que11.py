l = [44, 43, 66, 69, 61, 38, 33, 49, 55]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]

print(l)