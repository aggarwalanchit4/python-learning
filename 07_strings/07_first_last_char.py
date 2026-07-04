name = input("Enter the name : ")
if name[0].upper() == "A":
    print("starts with A")
else :
    print("doesnt start with A")

name = input("Enter the name : ")
if name[-1].upper() == name[0].upper():
    print("same")
else :
    print("not same")

name = str(input())
if name[-1].upper() == "T":
    print("end with t")
else:
    print("dosent end with t")

name = str(input())
if name[-1].upper() == name[0].upper():
    print("same")
else:
    print("not same")
