#Arbitrary keyword argument
def student_details(**details):
    print(details)

    for key,value in details.items():
        print(key,":",value)




student_details(Name='Joel Roy',Rollno='1',Place='Koothattukulam')