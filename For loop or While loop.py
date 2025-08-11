list=[]
count=0
while True:      # We use while because it gives infinite loops/chances
     numb=int(input("Enter the number"))
     if numb>5 and numb<25:
      list.append(numb)
      count=count+1
      print(numb)
      print(list)
     else:
        print("You entered the wrong number")
     if count>=5:
      break

