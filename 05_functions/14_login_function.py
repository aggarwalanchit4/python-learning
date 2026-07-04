
def login():
    username = input("Enter username: ")
    passw = int(input("Enter password: "))

    if username == "anchit" and passw == 12345:
        print("Login Successful")
    else:
        print("Invalid username or password")

login()

def login():
    for i in range(3):

        username = input("Enter username: ")
        passw = str(input("Enter password: "))

        if username == "anchit" and passw == "12345":
            print("Login Successful")
            break
        else:
            print("Invalid username or password")

login()
