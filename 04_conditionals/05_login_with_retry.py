#enter correct password
email = str(input("enter email :"))
password = str(input("enter passsword :"))
if(email=="aggarwalanchit4" and password=="12345"):
    print("login successfull")
elif(email!="aggarwalanchit4" and password!="12345"):
    print("wrong email and password")
    email = str(input("enter email again :"))
    password = str(input("enter passsword again :"))
    if(email=="aggarwalanchit4" and password=="12345"):
            print("login succesfull")
    else:
         print("login failed")
