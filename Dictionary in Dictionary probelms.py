student_dict={'kai':{'phy':89,'che':99,'maths':89,'cs':90},
             'fanum':{'phy':78,'che':94,'maths':79,'cs':92},
              'ray':{'phy':88,'che':70,'maths':80,'cs':91}}

for stu,marks in student_dict.items():  #To get the keys and values
    total=0
    for mark in marks.values():         # To get rhe values only

      total=total+mark


      print(f"the total marks  of {stu} is {total}")
      print(f"the average mark of {stu} is {total/4} ")


