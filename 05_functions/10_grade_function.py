def grades(x):
    if 90<= x <=100:
        print("A")
    elif 75<=  x <90:
        print("B")
    elif  60<= x <75:
        print("C")
    else:
        print("Fail")
grades(80)
grades(90)
grades(77)
grades(55)

def student_result(marks):
    if 90 <= marks <= 100 :
        print("Grade A")
    elif 75 <= marks < 90 :
        print("Grade B")
    elif 60 <= marks < 75 :
        print("Grade C")
    else :
        print("Fail")

student_result(80)  
