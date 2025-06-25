#Arbitrary Positional argument
def sum_num(*a):
    print(a)
    sum=0
    for i in a:
       sum=sum+i
       print(sum)

sum_num(1,2,3,4,5,6,7,8,9,10)
