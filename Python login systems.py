user_name=['a','b','c','d']
password=['abc','xyz','123','abc@123']


user_typing=input("Enter the username")
index=0
for u in user_name:
   if user_typing==u:
      user_password=input("Enter the password")
      if user_password==password[index]:
         print("Welcome",u)
      else:
         print("Wrong password")
      break
   index = index + 1
else:
   print("No user found")




