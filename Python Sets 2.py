num1={1,2,3,4,5}
num2={4,5,6,7,8}
union_set=num1.union(num2)    # Union of sets
print(union_set)

intersection_set=num1.intersection(num2)   # Intersection of sets
print(intersection_set)


difference_set=num1.difference(num2)        #The difference between two sets
print("The diffrence is",difference_set)


for i in union_set:
    print(i)