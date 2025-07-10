Emp_salary={'maxi':50000,'ray':20000,'joel':100000}
print(type(Emp_salary))
print(Emp_salary["joel"])
Emp_salary['kai']=200000
Emp_salary['fanum']=300000
Emp_salary.__setitem__('speed',10000000)
print(Emp_salary)
