Names={'joel':'1234','kai':'456','ray':'789'}
user_typing=input("Enter the username")
if user_typing in Names.keys():
    password=input("Enter your password")
    if password==Names[user_typing]:
        print("Welcome",user_typing)
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


