d = {}
n = int(input("Enter N: "))

for i in range(1, n+1):
    d[i] = i*i

print(d)

d1 = {1: "Dhvanit", 2: "Jainish", 3: "Meet", 4: "Rahul", 5: "Aarti"}

sname = input("Enter Student Name To Search In Dictionary: ")
flag = False

for i in d:
    if sname==d[i]:
        flag=True
        break
if flag == True:
    print("Present")
else:
    print("Absent")