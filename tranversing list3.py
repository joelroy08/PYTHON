#Q) Find the average of the numbers from the list
i=1
limit=5
list_0=[]
while i<=limit:
    list_1=int(input("Enter the number"))
    list_0.append(list_1)
    i=i+1
    print(list_0)
#Reading the input from the list
k=0
while k<len(list_0):
    print(list_0[k])
    k=k+1
#Calculating the average of the list
j=0
sum=0
while j<len(list_0):
  sum=sum+list_0[j]
  j=j+1
  average=sum/len(list_0)
  print("The average of the number is",average)