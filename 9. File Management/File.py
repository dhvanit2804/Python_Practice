file=open("tops1.txt","w")
file.write("Welcome To File Management Concept Using Python")
file.close()
print("File Writen Successfully")
print("****************************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("****************************************************")

file=open("tops1.txt","a")
file.write("\nFile Management With Python Is Very Easy To Learn")
file.close()
print("****************************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("****************************************************")

'W+ Means write and read both together'
file=open("tops2.txt","w+")
file.write("This is w+ operation using python")
print("File Current Position : ",file.tell())
file.seek(0)
print("File Data: ",file.read())
file.close()
print("****************************************************")