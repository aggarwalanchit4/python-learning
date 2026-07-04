name = input("Enter the name : ") 
count_a = 0
for ch in name:
     if ch.lower() == "a":
        count_a = count_a + 1
    
    
print(count_a)

name = input("Enter the name : ")
count_a = 0

for ch in name:
    if ch.lower() not in ("a", "e", "i", "o", "u"):
        
        count_a = count_a + 1

print(count_a)

name = input()
count = 0
for ch in name :
    if ch.isalpha and ch.lower() in ("a" , "e" , "i" , "o" , "u"):
        count = count+1


print(count)

name = input()
count = 0
for ch in name :
    if ch.isalpha() and ch.lower() not in ("a" , "e" , "i" , "o" , "u"):
        count = count+1

print(count)
