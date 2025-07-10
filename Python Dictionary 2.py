employees_salary={'joel':10000,'max':20000,'ray':3000,'kai':400000,'fanum':80000}
print(employees_salary)
employees_salary_dup=employees_salary.copy() #To create a duplicate of the dictionary for further use
print(employees_salary_dup)
popped_item=employees_salary.popitem()  #To remove the last element from the dictionary
print(popped_item)
print(employees_salary)
employees_salary.pop('joel')  #To remove the specific element from the dictionary
print(employees_salary)
print(employees_salary_dup)
employees_salary.values()
print(employees_salary.values())  #To print the values in the dictionary
for i in employees_salary.values(): # To iterate the values in the dictionary
    print(i)


employees_salary.keys()     #To print the keys in the dictionary
print(employees_salary.keys())
for j in employees_salary.keys(): #To iterate the keys in the dictionary
    print(j)
employees_salary.clear()
print(employees_salary)  #To clear the dictionary completely

