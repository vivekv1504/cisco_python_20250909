employees=[]
employee=("vivek",22,33000,True)
employees.append(employee)
employee=("jaya",23,35000,True)
employees.append(employee)
employee=("sai",21,38000,True)
employees.append(employee)
I=0
search='sai'
index=-1
for emp in employees:
    if emp[0]==search:
        index=I
        break
    I+=1
if index == -1:
    print('employee not found')
else:
    search_employee = employees[index]
    print(search_employee)
    salary=float(input('salary:'))
    employee = (search_employee[0],search_employee[1],search_employee[2])
    employees[index]=employee
    print('after search and update:',employees)
employee=('dravid',50,2000.75,True)
employees.append(employee)
print('after add dravid:',employees)
employees.pop()
print('after delete dravid:',employees)
position = 1
employees.pop(position)
print('after delete vivek:',employees)
