name = input("Enter the name : ")
count = 0
for i in range(len(name)):
    if name[i]  == name[i].upper():
            count = count + 1

print(count)

name = input("Enter the name : ")
count = 0
for i in range(len(name)):
    if name[i]  == name[i].lower():
            count = count + 1

print(count)
