try:
    number = int(input("ente a number:"))
    print(1/number)
except ZeroDivisionError:
    
    print("numbrer can not be divided by zero")
except ValueError:
    print("you have to provide correct value")
finally:
    print("program is over")
