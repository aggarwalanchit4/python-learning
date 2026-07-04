def bonus(salary):
    if salary < 20000 :
        bon = (20/100)*salary
        print(f"Bonus = {bon}")
    elif salary < 50000 :
        bon = (10/100)*salary
        print(f"Bonus = {bon}")
    elif  50000 <= salary :
        bon = (5/100)*salary
        print(f"Bonus = {bon}")

bonus(60000)
