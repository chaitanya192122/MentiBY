UserName=input("User Name : ")
PassWord=input("Password : ")

if UserName== "admin":
    if PassWord=="1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect UserName")