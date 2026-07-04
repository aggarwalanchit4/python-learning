try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == '+':
        print("Result =", a + b)
    elif op == '-':
        print("Result =", a - b)
    elif op == '*':
        print("Result =", a * b)
    elif op == '/':
        print("Result =", a / b)
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Please enter valid numbers")
