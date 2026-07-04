#grade marking
m1 = int(input("enter student marks1 : "))
m2 = int(input("enter student marks2 : "))
m3 = int(input("enter student marks3 : "))
m4 = int(input("enter student marks4 : "))
m5 = int(input("enter student marks5 : "))
percentage=((m1+m2+m3+m4+m5)*100)/500
print("percentage =  ", percentage)
if(percentage>=90):
    print("grade A")
elif(75<=percentage<=90):
    print("grade B")
elif(60<=percentage<=75):
    print("grade C")
elif(45<=percentage<=60):
    print("grade B")
elif(30<=percentage<=45):
    print("grade E")
else:
    print("fail")
