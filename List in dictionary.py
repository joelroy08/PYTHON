emp_salary={} #Dictionary
name=['joel','kai','ray']
salary=[1000,100001,20000]
for i in range(len(name)):
    key=name[i]
    value=salary[i]
    emp_salary[key]=value
print(emp_salary)